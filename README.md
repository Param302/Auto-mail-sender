# Auto Cold Email Sender

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0.0-red)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0.0-green)
![DeepSeek](https://img.shields.io/badge/DeepSeek-1.0.0-yellow)

## About the Project

Auto Cold Email Sender is a Streamlit-based application that automates the process of sending cold emails. Users can input their email credentials, API keys, and other necessary information to generate and send personalized emails to multiple recipients.

## Workflow

1. **Input Credentials**: Users provide their email, app password, and OpenAPI/DeepSeek API key.
2. **Upload Data**: Users can upload a CSV file with columns for company names, emails, and positions, paste the CSV content, or manually enter data for up to 10 emails.
3. **Add Personal Information**: Users add information about themselves, upload their resume, and provide optional keywords.
4. **Generate Email Template**: Click the generate button to create an editable email template.
5. **Send Emails**: After reviewing and editing the template, click the send button to send the emails.

## User Flow

1. **Landing Page**: The user is greeted with a landing page where they can start the process.
2. **Credentials Page**: The user inputs their email, app password, and API keys.
3. **Data Input Page**: The user can choose to upload a CSV file, paste CSV content, or manually enter data.
4. **Personal Information Page**: The user adds personal information, uploads their resume, and provides optional keywords.
5. **Email Template Page**: The user clicks the generate button to create an email template, which they can edit.
6. **Review and Send Page**: The user reviews the email template and clicks the send button to send the emails.
7. **Confirmation Page**: The user receives a confirmation that the emails have been sent successfully.

## Tech Stack

- **Python**: The core programming language used for the application.
- **Streamlit**: Used for creating the web interface.
- **OpenAPI/DeepSeek**: APIs used for generating email content.
- **smtplib**: Used for sending emails.

## Requirements

- Python 3.10
- Streamlit 1.0.0
- OpenAPI/DeepSeek API key
- Email credentials (email and app password)

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/auto-cold-email-sender.git
    cd auto-cold-email-sender
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit application:
    ```sh
    streamlit run main.py
    ```

4. Follow the workflow steps to input your data and send emails.

## Contact

For any questions or issues, please contact [Parampreet Singh](mailto:connectwithparam.30@gmail.com).

