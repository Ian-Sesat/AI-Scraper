# Automated Job Outreach System
This project automates the process of sending personalized messages to companies based on job listings scraped from various job boards.
## Installation
To run this project, you need to install the following dependencies:
- `jobspy`: A package for scraping job listings from various job boards.
- `pandas`: A library for data manipulation and analysis.
- `smtplib`: A library for sending emails using SMTP.
- `email`: A library for handling email messages.
- `re`: A module for regular expressions.
You can install these dependencies using pip:
```bash
pip install -U python-jobspy

## Usage
Run the scrape_jobs script to scrape job listings and save them to a CSV file.It also prepares the messages to be sent and gives ouptut in the emails.txt file.
Run the send_emails script to send personalized messages to companies based on the scraped job listings.

## Configuration
Before running the send_emails script, make sure to:
Replace 'your.email@gmail.com' and 'your_password': Replace these placeholders with your Gmail email address and password.
Adjust the jobs.csv file path: If the jobs.csv file is located in a different directory, update the file path accordingly.
