# Email Sender with Attachment

This script demonstrates how to send an email with an attachment using Python. It leverages the `smtplib` library to handle the SMTP protocol and the `email` library to create the email content and attach files.

## Prerequisites

- Python 3.x installed on your machine
- An SMTP server (Gmail is used in this example)
- The sender's email credentials (email address and app password)
- The file you want to attach

## Setup

1. **Install Required Libraries**: The script uses standard Python libraries (`smtplib` and `email`), so no additional installations are required.

2. **Enable Less Secure Apps**: If you're using Gmail, you may need to allow less secure apps to send emails using your account. Go to your Google Account settings and enable "Less secure app access." Alternatively, you can use an app-specific password.

3. **Configure the Script**:
   - Set the `sender_email` and `sender_password` variables with your email address and app password.
   - Ensure the `file_name` points to the correct file you want to attach.

## Usage

1. **Run the Script**:
   - Execute the script using Python.
   - When prompted, enter the recipient's email address.

2. **Example**:
   ```
   python send_email.py
   ```

3. **Expected Output**:
   - The script will send an email with the specified subject and body, along with the attached file, to the recipient.

## Code Explanation

- **Import Libraries**:
  - `smtplib`: For sending emails using the SMTP protocol.
  - `MIMEMultipart`, `MIMEText`, `MIMEApplication`: For creating the email structure and attaching files.

- **Set Up Email Parameters**:
  - `sender_email`: The email address of the sender.
  - `sender_password`: The app password for the sender's email.
  - `recipient_email`: The email address of the recipient.

- **Create Email Content**:
  - A `MIMEMultipart` object is created for the email message.
  - The body of the email is attached as an HTML MIME part.
  - The file to be attached is read and added as a MIME application part.

- **Send the Email**:
  - The script connects to the SMTP server, starts TLS for security, logs in, and sends the email with the attachment.

## Error Handling

- The script includes basic error handling to catch and print any exceptions that occur during the email-sending process.

## Important Notes

- Be cautious when using your email credentials in scripts. Consider using environment variables or secure storage solutions to protect sensitive information.
- Avoid sharing your email credentials and app passwords in public repositories or with others.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---