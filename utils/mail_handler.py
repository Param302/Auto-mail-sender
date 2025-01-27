import smtplib

class EmailSender:

    def __init__(self, email, password):
        self.email = email
        self.__password = password
    

    def __call__(self, receiver_email, subject, message):
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.email, self.__password)
            msg = f"Subject: {subject}\n\n{message}"
            server.sendmail(self.email, receiver_email, msg)
            return 0
        return 1


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    load_dotenv()

    send_email = EmailSender(EMAIL, PASSWORD)
    send_email("connectwithparam.30@gmail.com", "Test", "Hello, this is a test email")