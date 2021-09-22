from deposit_funds import deposit_funds
from flask_script import Manager
from app import app


manager = Manager(app)
def make_deposit():
    deposit_funds