import os
import tkinter as tk
from tkinter import filedialog, messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import pandas as pd
from PIL import Image, ImageTk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

win_size_x = 600
win_size_y = 600
logo_x = 50
logo_y = 50


class EmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Sender App")

        # Get the path of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Load and set the background image
        background_image_path = os.path.join(script_dir, "es_logo.png")  # Replace with the name of your image file
        self.background_image = Image.open(background_image_path)
        # Resize the image to 30x30 pixels
        small_image = self.background_image.resize((logo_x, logo_y), Image.ANTIALIAS)
        # Convert the resized image to Tkinter PhotoImage
        self.small_image_photo = ImageTk.PhotoImage(small_image)

        # Create a list to store successfully sent email addresses
        self.successful_emails = []
        self.initialize_gui()

    def initialize_gui(self):
        # Create a frame to hold the main content
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a label for the upper right corner to display the small image
        small_image_label = tk.Label(main_frame, image=self.small_image_photo)
        small_image_label.image = self.small_image_photo
        small_image_label.grid(row=0, column=1, padx=0, pady=10)

        # Add content to the GUI
        self.add_content(main_frame)

    def add_content(self, frame):
        row_counter = 1

        # User Email
        email_row = row_counter + 1

        tk.Label(frame, text="Your Email:").grid(row=email_row,sticky=tk.W, column=0, padx=5, pady=5)
        self.user_email_entry = tk.Entry(frame, width=40)
        self.user_email_entry.grid(row=email_row, column=1, padx=0, pady=5)

        # User Password
        pass_row = row_counter + 2
        tk.Label(frame, text="Your Password:").grid(row=pass_row, column=0, sticky=tk.W, padx=5, pady=5)
        self.user_password_entry = tk.Entry(frame, show="*", width=40)
        self.user_password_entry.grid(row=pass_row, column=1, padx=0, pady=5)

        # Group Email
        group_mail = row_counter + 3
        tk.Label(frame, text="Group Email:").grid(row=group_mail, column=0, sticky=tk.W, padx=5, pady=5)
        self.group_email_entry = tk.Entry(frame, width=40)
        self.group_email_entry.grid(row=group_mail, column=1, padx=0, pady=5)

        # Group Email
        bcc_mail = row_counter + 4
        tk.Label(frame, text="BCC Email (comma-separated):").grid(row=bcc_mail, column=0, sticky=tk.W, padx=5, pady=5)
        self.bcc_email_entry = tk.Entry(frame, width=40)
        self.bcc_email_entry.grid(row=bcc_mail, column=1, padx=0, pady=5)

        # Email Title
        title_row = row_counter + 5
        tk.Label(frame, text="Email Title:").grid(row=title_row, column=0, sticky=tk.W, padx=5, pady=5)
        self.title_entry = tk.Entry(frame, width=40)
        self.title_entry.grid(row=title_row, column=1, padx=0, pady=5)

        # Email Body
        body_row = row_counter + 6
        tk.Label(frame, text="Email Body:").grid(row=body_row, column=0, sticky=tk.W, padx=5, pady=5)
        self.body_entry = tk.Text(frame, height=7, width=40)
        self.body_entry.grid(row=body_row, column=1, padx=0, pady=5)

        # csv Sheet
        csv_row = row_counter + 7
        tk.Label(frame, text="CSV Sheet:").grid(row=csv_row, column=0, sticky=tk.W, padx=5, pady=5)
        self.csv_path_entry = tk.Entry(frame, width=40)
        self.csv_path_entry.grid(row=csv_row, column=1, padx=0, pady=5)
        tk.Button(frame, text="Browse", command=self.browse_csv).grid(row=csv_row, column=2, padx=0, pady=5)

        # Certificates Folder
        cer_row = row_counter + 8
        tk.Label(frame, text="Certificates Folder:").grid(row=cer_row, column=0, sticky=tk.W, padx=5, pady=5)
        self.certificates_path_entry = tk.Entry(frame, width=40)
        self.certificates_path_entry.grid(row=cer_row, column=1, padx=0, pady=5)
        tk.Button(frame, text="Browse", command=self.browse_certificates).grid(row=cer_row, column=2, padx=0, pady=5)

        # Send Button
        send_row = row_counter + 9
        tk.Button(frame, text="Send Emails", command=self.send_emails).grid(row=send_row, column=0, columnspan=3, pady=10)

        # Create a Listbox to display successful email addresses
        self.successful_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.successful_listbox.pack(pady=10, expand=True)

        # Create a Scrollbar and link it to the Listbox
        scrollbar = tk.Scrollbar(root, command=self.successful_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.successful_listbox.config(yscrollcommand=scrollbar.set)

    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.csv_path_entry.delete(0, tk.END)
        self.csv_path_entry.insert(0, file_path)

    def browse_certificates(self):
        folder_path = filedialog.askdirectory()
        self.certificates_path_entry.delete(0, tk.END)
        self.certificates_path_entry.insert(0, folder_path)

    def send_emails(self):
        # Get values from the GUI
        user_email = self.user_email_entry.get()
        user_password = self.user_password_entry.get()
        group_email = self.group_email_entry.get()
        bcc_emails = [bcc.strip() for bcc in self.bcc_email_entry.get().split(',') if bcc.strip()]
        email_title = self.title_entry.get()
        email_body = self.body_entry.get("1.0", tk.END)
        csv_path = self.csv_path_entry.get()
        certificates_folder = self.certificates_path_entry.get()

        try:
            df = pd.read_csv(csv_path)
        except pd.errors.EmptyDataError:
            self.show_error("Error", "The selected CSV file is empty.")
            return

        # Connect to SMTP server
        smtp_server = "smtp.office365.com"
        port = 587

        success_emails=0
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(user_email, user_password)
            
            # Iterate over rows in the csv
            for index, row in df.iterrows():
                try:
                    recipient_email = row['email_column']  # replace 'email_column' with the actual column name
                    certificate_path = f"{certificates_folder}/{row['file_name']}"  # replace 'file_name' with the actual column name
                    # print(f"{index}: Sending email to {recipient_email}, the certificate path is: {certificate_path}")

                    # Create message
                    msg = MIMEMultipart()
                    if group_email:
                        msg['From'] = group_email
                    else:
                        msg['From'] = user_email
                    msg['To'] = recipient_email
                    msg['Subject'] = email_title
                    if bcc_emails:
                        msg['Bcc'] = ', '.join(bcc_emails)

                    # Replace placeholders in the email body
                    formatted_body = email_body.replace('{name}', f'<b>{row["name_column"]}</b>')
                    msg.attach(MIMEText(formatted_body, 'html'))

                    # Attach certificate
                    with open(certificate_path, "rb") as file:
                        attachment = MIMEApplication(file.read(), _subtype="pdf")
                        attachment.add_header('Content-Disposition', f'attachment; filename={row["file_name"]}')
                        msg.attach(attachment)

                    # Send email
                    recipients= [recipient_email] + bcc_emails
                    server.sendmail(user_email, recipients, msg.as_string())
                    # Update the listbox with the successful email address
                    self.successful_emails.append(recipient_email)
                    self.update_successful_listbox()

                    success_emails+=1
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    self.show_error("Error", f"An error occurred: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            self.show_error("Error", f"An error occurred: {str(e)}")
        finally:
            server.quit()
        messagebox.showinfo("Success",f"{success_emails} has been sent")

    def show_error(self, title, message):
        tk.messagebox.showerror(title, message)

    def update_successful_listbox(self):
        # Clear the listbox
        self.successful_listbox.delete(0, tk.END)

        # Update the listbox with successful email addresses
        for email in self.successful_emails:
            self.successful_listbox.insert(tk.END, email)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{win_size_x}x{win_size_y}")
    app = EmailSenderApp(root)
    root.mainloop()
