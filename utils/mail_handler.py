import os
import re
import smtplib
import dns.resolver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class EmailSender:

    def __init__(self, email, password):
        self.email = email
        self.__password = password
        self._server = self.connect_to_server()

    def connect_to_server(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.__password)
        return server

    def _is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def __call__(self, receiver_email, subject, message, pdf=None):
        if not self._is_valid_email(receiver_email):
            print(f"Invalid email address: {receiver_email}")
            return -1

        if not self._server:
            self._server = self.connect_to_server()

        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, "plain"))

        if pdf:
            with open(pdf, "rb") as attachment:
                pdf_part = MIMEApplication(attachment.read(), _subtype="pdf")
                pdf_part.add_header(
                    "Content-Disposition", f"attachment; filename= {os.path.basename(pdf)}")
                msg.attach(pdf_part)

        try:
            self._server.sendmail(self.email, receiver_email, msg.as_string())
            return 0
        except Exception as e:
            print(f"Error: {e}")
            return 1

    def __del__(self):
        self._server.quit()


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    MAIL_SUBJECT = os.getenv("HR_SUBJECT_1")
    MAIL_BODY = os.getenv("REFERRAL_BODY_1")
    print(EMAIL, PASSWORD, MAIL_SUBJECT, MAIL_BODY)
    load_dotenv()

    send_email = EmailSender(EMAIL, PASSWORD)
    send_email("abcd.efgh+123@gmail.com", MAIL_SUBJECT, MAIL_BODY,
               pdf="Resume - Parampreet Singh.pdf")
