import os
import random
import smtplib
from email.message import EmailMessage

name = "benedict cumberbatch"

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

# The mailing list of unfortunate users
emails = ['emails go here']

def mutate_global_name(name):
    for c in range(random.choice([0, 1, 1, 2, 2]), len(name), random.choice([3, 4, 5])):
        if name[c] in vowels:
            name = name[:c] + random.choice(vowels) + name[c + 1 :]
        elif name[c] in consonants:
            name = name[:c] + random.choice(consonants) + name[c + 1 :]

    return name

def create_email_with_contents(content):
    message = EmailMessage()
    message.set_content(
        'Today\'s disaster:'
        + '\n'
        + content)
    return message

def set_email_subject_and_sender(message):
    message['Subject'] = 'Your Daily Cumberbot'
    message['From'] = 'Persistent Benedict Cumberbot'

def set_email_recipient(message, name):
    message['To'] = name

def send_email_to_mailing_list():
    print('Sending emails')
    try:
        # Setup server  
        print('Setting up server')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(os.environ['CUMBY_USER'], os.environ['CUMBY_PASS'])

        # Generating message
        content = mutate_global_name(name)

        # Dispatch message
        print('Dispatching message')
        for recipient in emails:
            message = create_email_with_contents(content)
            set_email_subject_and_sender(message)
            set_email_recipient(message, recipient)
            server.send_message(message)        
    except Exception as e:  
        print('Something went wrong: ' + str(e))
    finally:
        print('Quitting server')
        server.quit()

send_email_to_mailing_list()
