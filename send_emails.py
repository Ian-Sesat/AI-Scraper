import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import re

# Function to validate email addresses that handles None and non-string inputs
def is_valid_email(email):
    if email is None or not isinstance(email, str):
        return False
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# Function to create personalized messages
def create_messages(df):
    messages = []
    for index, row in df.iterrows():
        message = f"Hi {row['company']}, we noticed that your company, {row['company']}, posted a job on {row['site']}. " \
                  f"Good news for your company – we have a candidate who fits this description perfectly. " \
                  f"He/she has [Qualifications]. Would you like to learn more? Please call me at [Phone Number] or " \
                  f"schedule a meeting using a calendar invite system like Calendly. Alternatively, you can provide " \
                  f"your phone number, and I'll contact you."
        messages.append({'email': row['emails'], 'message': message})
    return messages

# Send email function
def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Start TLS for security
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    # Login with sender email credentials
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Quit server
    server.quit()

# Assuming you have a dataframe `jobs_df` with job listing data
jobs_df = pd.read_csv('jobs.csv')

# Assuming 'emails' column exists; if not, adjust data gathering/entry to include it
# Filter out rows without valid emails
valid_emails_df = jobs_df[jobs_df['emails'].apply(is_valid_email)]

# Generate messages for valid email entries
messages_to_send = create_messages(valid_emails_df)

# Email sender credentials
sender_email = "your.email@gmail.com"
sender_password = "your_password"   # Use an app-specific password if 2-factor authentication is enabled

# Send messages
for message_info in messages_to_send:
    recipient_email = message_info['email']
    message = message_info['message']
    subject = "Regarding Job Posting"

    # Send email
    send_email(sender_email, sender_password, recipient_email, subject, message)
    print(f"Email sent to {recipient_email}.")

print("All emails have been sent.")
