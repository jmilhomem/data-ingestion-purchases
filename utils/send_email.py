"""Send E-mails."""
import smtplib

from email.message import EmailMessage


def send_email(subject, recipient, to, content, user, password):
    """Send e-mails by gmail domain.

    :param subject: string -> e-mail subject
    :param recipient: string -> e-mail recipient
    :param: string -> who will recieve the e-mail
    :param: string -> the e-mail content
    :param: string -> the gmail e-mail account
    :param: string -> the google's app password
    """ 
    email = EmailMessage()

    email['Subject'] = subject
    email['From'] = recipient
    email['To'] = to   

    email.set_content(content)    

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(user, password)    

    s.send_message(email)
    s.quit()
