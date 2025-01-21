import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(to_email, subject, body):
    # Your Gmail credentials
    gmail_user = "youremail@gmail.com"
    gmail_password = "your_app_password"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to the server
        server.login(gmail_user, gmail_password)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(gmail_user, to_email, text)
        
        # Close the SMTP server
        server.quit()
        
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
