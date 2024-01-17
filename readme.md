# Email Sender App User Manual

## Introduction

Welcome to the Email Sender App! This application allows you to send emails to students, personalized with information from an CSV sheet and attached certificates. Follow the guide below to get started.

## Table of Contents

1. [Installation](#1-installation)
2. [Getting Started](#2-getting-started)
3. [User Interface Overview](#3-user-interface-overview)
4. [Sending Emails](#4-sending-emails)
5. [CSV File Format](#5-csv-file-format)
6. [Handling Two-Factor Authentication (2FA)](#5-handling-two-factor-authentication-2fa)
7. [Troubleshooting](#6-troubleshooting)
8. [Feedback and Support](#7-feedback-and-support)

## 1. Installation

Ensure that you have the required dependencies installed:

- Python 3.x
- Tkinter (included with most Python installations)
- Pillow library (`pip install Pillow`)

Download the Email Sender App files and place them in a dedicated folder.

## 2. Getting Started

1. Open a terminal or command prompt.
2. Navigate to the folder containing the Email Sender App files.
3. Run the app by executing the command: `python email_sender_app.py`

## 3. User Interface Overview

The Email Sender App has a simple and intuitive interface. Here's an overview:

- **Your Email:** Enter your email address.
- **Your Password:** Enter the password for your email account.
- **Group Email (Optional):** Enter a group email address (optional).
- **BCC Email (comma-separated)(Optional):** Optionally, provide BCC email addresses separated by commas (Optional).
- **Email Body:** Compose your email body, and use HTML format. The email content should inclide the placeholders for personalized information.
- **CSV Path:** Click "Browse" to select the CSV containing student information.
- **Certificates Path:** Click "Browse" to choose the folder containing certificates.
- **Send Emails Button:** Click to start the email sending process.

## 4. Sending Emails

1. **User Authentication:**

   - Enter your email address and password.
   - Optionally, provide a group email address and BCC email addresses (comma-separated).

2. **Email Configuration:**

   - Enter the email subject/title and compose the email body using placeholders (e.g., `{name}`).
   - Browse and select the CSV file containing recipient information.
   - Browse and select the folder containing individual certificates.

3. **Sending Emails:**

   - Compose your email body using HTML formatting for bold words (e.g., `<b>{name}</b>`).
   - Click the "Send Emails" button.
   - The application will iterate through the CSV data, replacing placeholders and sending personalized emails.
   - A success message will be displayed upon completion.

4. **Successful Emails:**
   - The listbox displays email addresses that were successfully sent.

The app will start sending personalized emails to students based on the CSV data.

## 5. CSV File Format

The CSV file must contain the following columns:

- **email_column:** Email addresses of recipients.
- **file_name:** Unique identifiers corresponding to certificate filenames.
- **name_column:** Names of recipients.

**Note:** Ensure that the column names are accurate and match the placeholders used in the email body.

## 6. Handling Two-Factor Authentication (2FA)

If your email account requires Two-Factor Authentication (2FA), follow these steps:

1. Log in to your email account and navigate to the security settings.
2. Generate an "App Password" specifically for the Email Sender App.
3. Use the generated App Password in the "User Password" field when running the application.
4. For more information follow [these steps](https://support.microsoft.com/en-us/account-billing/create-app-passwords-from-the-security-info-preview-page-d8bc744a-ce3f-4d4d-89c9-eb38ab9d4137).

## 7. Troubleshooting

- If you encounter errors, check the console for error messages.
- Ensure that the provided paths for CSV and certificates are correct.
- Confirm that your email credentials are accurate.
- Check your email provider's settings for any restrictions.

## 8. Feedback and Support

We value your feedback! If you encounter issues or have suggestions for improvements, please contact me [yasmin.elderiny@egyptscholars.org](mailto:yasmin.elderiny@egyptscholars.org).

Thank you for using the Email Sender App!
