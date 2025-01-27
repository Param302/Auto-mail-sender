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
    