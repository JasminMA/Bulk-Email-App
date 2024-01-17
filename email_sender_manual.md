# Email Sender App User Manual

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Instructions](#instructions)
   - [Running the Application](#running-the-application)
   - [User Authentication](#user-authentication)
   - [Email Configuration](#email-configuration)
   - [Sending Emails](#sending-emails)
   - [Successful Emails](#successful-emails)
4. [CSV File Format](#csv-file-format)
5. [Handling Two-Factor Authentication (2FA)](#handling-two-factor-authentication-2fa)
6. [Contact Information](#contact-information)

## Overview

The Email Sender App is a user-friendly tool designed to simplify the process of sending personalized emails with certificates to multiple recipients. This manual provides step-by-step instructions on how to use the application efficiently.

## Features

- **User Email:** Enter your email address.
- **User Password:** Provide the password for your email account.
- **Group Email:** Optionally, specify a group email address.
- **BCC Email (comma-separated):** Optionally, add BCC email addresses separated by commas.
- **Email Title:** Enter the subject/title of the email.
- **Email Body:** Compose your email body, and use HTML format. The email content should inclide the placeholders for personalized information.
- **CSV Sheet:** Browse and select the CSV file containing recipient information.
- **Certificates Folder:** Browse and select the folder containing individual certificates.
- **Send Emails:** Click to send personalized emails to recipients.

## Instructions

### Running the Application

1. **Execution:**

   - Double-click the "Email_Sender_App.exe" file to launch the application.
   - The main window will appear, providing fields to input necessary email details.

2. **User Authentication:**

   - Enter your email address and password in the respective fields.
   - Optionally, specify a group email address and BCC email addresses (if needed).

3. **Email Configuration:**

   - Enter the subject/title and compose the email body using placeholders (e.g., `{name}`).
   - Browse and select the CSV file containing recipient information.
   - Select the folder containing individual certificates.

4. **Sending Emails:**

   - Click the "Send Emails" button to initiate the sending process.
   - The application will process the CSV data, replace placeholders, and send personalized emails.

5. **Successful Emails:**
   - The listbox displays email addresses that were successfully sent.

## CSV File Format

The CSV file must contain the following columns:

- **email_column:** Email addresses of recipients.
- **file_name:** Unique identifiers corresponding to certificate filenames.
- **name_column:** Names of recipients.

**Note:** Ensure that the column names in the CSV file match the placeholders used in the email body.

## Handling Two-Factor Authentication (2FA)

If your email account requires Two-Factor Authentication (2FA), follow these steps:

1. Log in to your email account and navigate to the security settings.
2. Generate an "App Password" specifically for the Email Sender App.
3. Use the generated App Password in the "User Password" field when running the application.
4. For more information follow [these steps](https://support.microsoft.com/en-us/account-billing/create-app-passwords-from-the-security-info-preview-page-d8bc744a-ce3f-4d4d-89c9-eb38ab9d4137).

## Feedback and Support

We value your feedback! If you encounter issues or have suggestions for improvements, please contact me [yasmin.elderiny@egyptscholars.org](mailto:yasmin.elderiny@egyptscholars.org).
