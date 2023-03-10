import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from app.outlook_email import OutlookEmail
from dotenv import load_dotenv


def run():
    load_dotenv()
    """This should call the email service depending on the config set"""
    email_service = OutlookEmail(
        os.getenv('OUTLOOK_USER', ''), os.getenv('OUTLOOK_TOKEN', '')
    )
    email_service.login()
    emails = email_service.get_unseen_emails(os.getenv('INBOX_NAME', 'inbox'))


if __name__ == '__main__':
    run()
