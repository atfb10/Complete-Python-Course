import smtplib
from email.message import EmailMessage

from credentials import EMAIL, PASSWORD

# Connect to port
PORT = 587
SMTP_CONNECTOR = smtplib.SMTP(host='smtp.gmail.com', port=PORT)
SMTP_CONNECTOR.starttls()
SMTP_CONNECTOR.login(EMAIL, PASSWORD)

EMAIL_CONTENT = '''Dear Adam,

I am sending you an email in Python. Hope it works!

Best,
Me
'''

# Generate the email
email = EmailMessage()
email['Subject'] = 'Test Email'
email['From'] = EMAIL
email['To'] = EMAIL
email.set_content(EMAIL_CONTENT)

# Send the email and then close the connection
SMTP_CONNECTOR.send_message(email)
SMTP_CONNECTOR.quit()