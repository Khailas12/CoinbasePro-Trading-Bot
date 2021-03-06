from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_FILE_NAME
from datetime import datetime
import logging
import boto3    # this package helps to acess AWS resource via Python



s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = 'us-east-2'
)

bucket_file_name = BUCKET_FILE_NAME


# Creates a logger with a FileHandler.
def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    # Creating file handler with log even debug msgs
    file_handler = logging.FileHandler('{}_{}.log'.format(logger_name, datetime.now().isoformat().split('.')[-1]))
    file_handler.setLevel(logging.DEBUG)
    
    # Creating the file handler and adding tp handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s %(message)s'
        )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler) # Adding the handler to logger
    
    
# Uploads the recently created log file to the designec file.
def upload_log(logger): 
    file_name = logger.handlers[0].baseFilename
    directory = datetime.now().date().isoformat()
    key = '{}/{}'.format(directory, file_name.split('/')[-1])
    
    bucket_name = BUCKET_FILE_NAME
    s3_client.upload_file(Filename = file_name, Bucket = bucket_name, Key=key)
    

# This is a decorator func that creates a logger, then passes it to the function and uploads the log file when it finishes.
def logger(func):
    def function_wrapper(*args, **kwargs):
        function_name = func.__name__
        log = create_logger(function_name)
        
        logger.info("Now Running - {}".format(function_name))

        resp = func(logger = log, *args, **kwargs)
        upload_log(logger)
        
        return resp
    return function_wrapper