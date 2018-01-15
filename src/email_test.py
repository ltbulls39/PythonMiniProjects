import smtplib
"""This simple app will send email messages from your own email"""

my_email = "YourEmailHere@gmail.com"
my_pass = "ShouldBeReplaced"

from_field = "WhoIsSendingThis@gmail.com"
to_field = "WhoIsRecievingThis@gmail.com"

message_body = "This can be replaced with whatever you want to send"
content = message_body

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()
# making secure
mail.starttls()

mail.login(my_email, my_pass)

#sending the email
mail.sendmail(from_field, to_field, content)
print("Message sent")
mail.quit()
