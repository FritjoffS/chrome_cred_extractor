import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, file_path):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Open the file in binary mode
    with open(file_path, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(file_path)}",
    )

    # Add attachment to message
    message.attach(part)

    # Convert message to string
    text = message.as_string()

    # Log in to server using secure context and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, text)

# Usage
sender_email = "info.verkstadsollebrunn@gmail.com"
sender_password = "Rmlza2FyczEw"  # Use an app password if you have 2FA enabled
receiver_email = "info.verkstadsollebrunn@gmail.com"
subject = "Text File Attachment"
file_path = "./textfile.txt"

send_email_with_attachment(sender_email, sender_password, receiver_email, subject, file_path)
print("Email sent successfully!")