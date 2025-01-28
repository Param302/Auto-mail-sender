import time
from utils.mail_handler import EmailSender


class AutoMailSender:
    """
    ---
    _If you want to follow this strategy and send mails, you can!_
    But make sure to setup ENV variables...
    -------

    Take Email & Password
    Read email IDs & company names from CSV file
    Send email to each email ID with the company name
    - Separate Mail body for HR (keywords: contact, hr, careers, etc...)
    - Separate Mail body for employers (referral)

    Multiple Subjects for HR & Employers to avoid spam
    Add Time delay between each email
    """

    def __init__(self, email, password):
        self.email = email
        self.__password = password
        self._reader = None
        self.current_hr_subject = 0
        self.current_hr_body = 0
        self.current_referral_subject = 0
        self.current_referral_body = 0
        self.mail_sender = EmailSender(email, password)

    def _load_csv(self, path):
        import csv
        f = open(path, "r")
        reader = csv.reader(f)
        next(reader)
        return reader

    def _get_records(self, n=10):
        return [next(self._reader) for _ in range(n)]

    def configure_templates(self, hr_template, referral_template):
        """
        Template (dict): {"subject": ["subject1", "subject2", ...], "body": ["body1", "body2", ...]}
        """
        self.hr_template = hr_template
        self.referral_template = referral_template
        self.total_hr_subjects = len(hr_template["subject"])
        self.total_hr_bodies = len(hr_template["body"])
        self.total_referral_subjects = len(referral_template["subject"])
        self.total_referral_bodies = len(referral_template["body"])

    def is_hr_mail(self, email):
        return any(keyword in email for keyword in ["contact", "hr", "career", "recruit", "job", "hiring", "hire", "future", "support"])

    def _update_sequence(self, is_hr=True):

        if is_hr:
            self.current_hr_subject, self.current_hr_body = (
                self.current_hr_subject + 1) % self.total_hr_subjects, (self.current_hr_body + 1) % self.total_hr_bodies
        else:
            self.current_referral_subject, self.current_referral_body = (
                self.current_referral_subject + 1) % self.total_referral_subjects, (self.current_referral_body + 1) % self.total_referral_bodies

    def send_mails(self, n=10, delay=5, pdf_path=None, *, records=None, filepath=None):
        if records is None:
            if self._reader is None:
                if filepath is None:
                    raise ValueError("Either provide records or filepath")
                self._reader = self._load_csv(filepath)
            records = self._get_records(n)
        print(records)
        for record in records:
            company, email = record
            if self.is_hr_mail(email):
                subject = self.hr_template["subject"][self.current_hr_subject]
                body = self.hr_template["body"][self.current_hr_body]
                self._update_sequence()
            else:
                subject = self.referral_template["subject"][self.current_referral_subject]
                body = self.referral_template["body"][self.current_referral_body]
                self._update_sequence(is_hr=False)

            subject = subject.replace("[company]", company.title())
            body = body.replace("[company]", company.title())
            self.mail_sender(email, subject, body, pdf=pdf_path)
            print(f"Mail sent to {email} with subject: {subject}")
            time.sleep(delay)

    def __del__(self):
        self._reader.close()
        self._reader = None
        del self.mail_sender
    
    @classmethod
    def close(cls): # Calls __del__ method
        del cls


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    HR_SUBJECTS = [sub for i in range(1, 6) if (
        sub := os.getenv(f"HR_SUBJECT_{i}"))]
    HR_BODIES = [body for i in range(1, 6) if (
        body := os.getenv(f"HR_BODY_{i}"))]

    REFERRAL_SUBJECTS = [sub for i in range(1, 6) if (
        sub := os.getenv(f"REFERRAL_SUBJECT_{i}"))]
    REFERRAL_BODIES = [body for i in range(1, 6) if (
        body := os.getenv(f"REFERRAL_BODY_{i}"))]

    hr_template = {"subject": HR_SUBJECTS, "body": HR_BODIES}
    referral_template = {"subject": REFERRAL_SUBJECTS, "body": REFERRAL_BODIES}

    mailer = AutoMailSender(EMAIL, PASSWORD)
    mailer.configure_templates(hr_template, referral_template)

    records = [
        ("Google", "abcdefgh@gmail.com"),
        ("Microsoft", "abcdefgh+hr@gmail.com"),
        ("Startup", "abcdefgh@gmail.com"),
        ("Amazon", "abcdefgh+careers@gmail.com"),
        ("Facebook", "abcdefgh@gmail.com"),
        ("LinkedIn", "abcdefgh@gmail.com"),
        ("Twitter", "abcdefgh@gmail.com"),
        ("Reddit", "abcdefgh@gmail.com"),
        ("X", "abcdefgh@gmail.com"),
        ("Y Combinator", "abcdefgh+contact@gmail.com"),
        ("Gemini", "abcdefgh+job@gmail.com"),
        ("Open AI", "abcdefgh+recruit@gmail.com")
    ]
    # mailer.send_mails(filepath="data.csv")
    mailer.send_mails(
        pdf_path="Resume - Parampreet Singh.pdf", records=records)
