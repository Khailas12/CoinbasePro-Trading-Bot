from dotenv import load_dotenv
import os


load_dotenv()

CB_CREDENTIALS = {
    'PASSPHRASE': os.getenv('CB_PASSPHRASE'),
    'SECRET': os.getenv('CB_SECRET'),
    'KEY': os.getenv('CB_KEY'),
    'URL': os.getenv('CB_URL')
}

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACESS_KEY')
BUCKET_FILE_NAME = os.getenv('BUCKET_FILE_NAME')