import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# Sender and receiver information
sender_email = "your_email_id@gmail.com"
sender_password = "2 step verification password/App password of your mail id"
recipient_email = input("enter the email id of receiver:")

# Create a MIMEMultipart message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = "There is a important mail with a attachment"

# Email body
body = """
<h4>Dear Sir/Madam,</h4>
<p>We have some thing for you,please enjoy</p>
<i style='text-align:center;'>thank you</i>
"""

# Attach the body with HTML format
message.attach(MIMEText(body,'html'))

# Attach a file
file_name = 'test.txt'
with open(file_name,'rb') as f:
    attachment = MIMEApplication(f.read())
    attachment.add_header('Content-Disposition','attachment',filename = file_name)
    message.attach(attachment)

# Send the email
try:
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.starttls()
        smtp.login(sender_email,sender_password)
        smtp.send_message(message)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")