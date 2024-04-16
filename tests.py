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

# Assuming you have a dataframe `jobs_df` with job listing data
# Example data loading (adjust as necessary based on your actual data loading method)
jobs_df = pd.read_csv('jobs.csv')

# Assuming 'emails' column exists; if not, adjust data gathering/entry to include it
# Filter out rows without valid emails
valid_emails_df = jobs_df[jobs_df['emails'].apply(is_valid_email)]

# Generate messages for valid email entries
messages_to_send = create_messages(valid_emails_df)

# Print messages for review (or connect to an email sending service)
for message_info in messages_to_send:
    print(f"Email: {message_info['email']}")
    print(f"Message: {message_info['message']}\n")
