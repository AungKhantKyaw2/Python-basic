# import smtplib

# sender = "aungkhantkyaw.didi@gmail.com"
# receiver = "miss.htet8.9@gmail.com"
# password = "izna qblg wshj jrde"
# subject ="Python email test"
# body  =  "I wrote an email for happiness"

# message = f""" From Snoop Dog{sender}
# To: Aung {receiver}
# Subject : {subject}\n
# {body}

# """
# try:
#  server = smtplib.SMTP("smtp.gmail.com",587)
#  server.starttls()
#  server.login(sender,password)
#  print("server logged in")
#  server.sendmail(sender,receiver,message)
#  print("email has been sent")

# except smtplib.SMTPAuthenticationError:
#      print("Unable to login")
 
# import smtplib, ssl
# from email.mime.text import MIMEText

# # Configuration
# smtp_server = "smtp.gmail.com"
# port = 465  # For SSL
# sender_email = "aungkhantkyaw.didi@gmail.com"
# receiver_email = "aung.kyaw@kmutt.ac.th"
# password = "fnly szlc apoy fdmt" 
# headers = {
#     "Subject": "Hello from Python",
#     "From": "sender@example.com",
#     "To": "hellohowareu@example.com"
# }


# # Create the email message
# message = MIMEText("This is the body of the email.")

# # Set headers from the dictionary
# for key, value in headers.items():
#     message[key] = value
# # # Create the email content
# # message = MIMEText("This is a plain text email.")
# # message["Subject"] = "Hello from Python"
# # message["From"] = sender_email
# # message["To"] = receiver_email

# # Send the email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message.as_string())

# print("Email sent successfully!")


