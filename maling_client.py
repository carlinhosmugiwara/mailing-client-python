import smtplib
from email.mime.multipart import MIMEMultipart # for the whole process
from email.mime.text import MIMEText # type of text used
from email.mime.base import MIMEBase # will be used for attachment
from email import encoders # will be used to encode the attachment

# setting up smtp server
smtp_server = smtplib.SMTP('smtp.gmail.com', 25) # make sure to find the right smtp provider, I'm using the google one here

# start server
smtp_server.ehlo()

#login into account
#I'm gonna put a generic e-mail and password, but make sure to never put your password directly in the code for safety purposes, always use a encrypted file
with open('mypassword.txt', 'r') as f:
  mypassword = f.read()
  smtp_server.login('my_email.gmail.com', mypassword)

# now the message
message = MIMEMultipart()
message['From'] = 'Whoever it is composing'
message['To'] = 'email.gmail.com' # I putted gmail here, but it can be any type of e-mail
message['Subject'] = 'The subject of the email'
# it is better to create a file with the email itself, in this case I'm gonna use the file myemail.txt
with open('myemail.txt', 'r') as f:
  myemail = f.read()
message.attach(MIMEText(myemail, 'plain'))

# now let's add an image attachment for things to get more interesting
myimage = 'myimage.jpg'
attachment = open(myimage, 'rb') # in this case "rb" needs to be used becaquse it is an image
base  = MIMEBase('application', 'octet-stream')
base.set_payload(attachment.read())
encoders.encode_base64(base)
base.add_header('Content-Disposition', f'attachment; filename={myimage}')

# attaching the image to the message 
message.attach(base)

# transform the message in  string
text = message.as_string()

# now let's send the email
smtp_server.sendmail('my_email.gmail.com', 'email.gmail.com', text)

