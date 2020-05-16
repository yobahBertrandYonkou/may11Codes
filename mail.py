import smtplib

#list of recipients
li = ["xxxx@gmail.com", "xxxx@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587) #making a connection to smtp server
    s.starttls() #starting transport layer security
    s.login("sender_email", "sender_gmail_pass") #logging in to sender's gmail account
    message = "Error in Jenkins siteTester Job" #message to be sent
    s.sendmail("sender_email", dest, message) #sends message
    s.quit() #closes connection to smtp server