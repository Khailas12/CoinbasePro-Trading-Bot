from dotenv import load_dotenv
import os


load_dotenv()

CB_CREDENTIALS = {
    'PASSPHRASE': os.getenv('CB_PASSPHRASE'),
    'SECRET': os.getenv('CB_SECRET'),
    'KEY': os.getenv('CB_KEY'),
    'URL': os.getenv('CB_URL')
}