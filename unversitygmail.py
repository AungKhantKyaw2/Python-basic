
# for outlook unversity email
# import smtplib
# import ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Configuration
# smtp_server = "smtp.gmail.com"
# port = 465  # For SSL
# sender_email = "aungkhantkyaw.didi@gmail.com"
# receiver_email = "aung.kyaw@kmutt.ac.th"
# password = "fnly szlc apoy fdmt"  # Use an app password if required

# # Create the email message
# message = MIMEMultipart()
# message["Subject"] = "Hello from Python"
# message["From"] = sender_email
# message["To"] = "bensat"

# # Email body
# body = "This is the body of the email."
# message.attach(MIMEText(body, "plain"))

# # Send the email
# context = ssl.create_default_context()
# try:
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#          server.login(sender_email, password)
#          server.sendmail(sender_email, receiver_email, message.as_string())

#          print("Email sent successfully!")
# except Exception as e:
#     print(f"Error sending email: {e}")
        
