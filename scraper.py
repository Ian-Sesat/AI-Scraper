from jobspy import scrape_jobs
import pandas as pd
import pandas as pd
import re

jobs: pd.DataFrame = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    search_term="data scientist",
    location="New York, NY",
    results_wanted=25,  # be wary the higher it is, the more likey you'll get blocked (rotating proxy can help tho)
    country_indeed="USA",
    # proxy="http://jobspy:5a4vpWtj8EeJ2hoYzk@ca.smartproxy.com:20001",
)

# formatting for pandas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", 50)  # set to 0 to see full job url / desc

# 1: output to console
print(jobs)

# 2: output to .csv
jobs.to_csv("./jobs.csv", index=False)
print("outputted to jobs.csv")

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

# Save messages to a text file
def save_messages_to_file(messages, filename='emails.txt'):
    with open(filename, 'w') as file:
        for message_info in messages:
            file.write(f"Email: {message_info['email']}\n")
            file.write(f"Message: {message_info['message']}\n\n")

# Assuming you have a dataframe `jobs_df` with job listing data
jobs_df = pd.read_csv('jobs.csv')

# Assuming 'emails' column exists; if not, adjust data gathering/entry to include it
# Filter out rows without valid emails
valid_emails_df = jobs_df[jobs_df['emails'].apply(is_valid_email)]

# Generate messages for valid email entries
messages_to_send = create_messages(valid_emails_df)

# Save the messages to a text file
save_messages_to_file(messages_to_send)
print("Messages have been saved to emails.txt.")

# Print messages for review (or connect to an email sending service)
for message_info in messages_to_send:
    print(f"Email: {message_info['email']}")
    print(f"Message: {message_info['message']}\n")
