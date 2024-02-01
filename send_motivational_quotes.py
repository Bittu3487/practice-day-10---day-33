import smtplib
import datetime as dt
import random
my_email = "debashisgoswami000@gmail.com"
my_password = "itya nxmb zqgv mtsw"
now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt","r") as quotes_file:
    quotes = quotes_file.readlines()
    quote = random.choice(quotes)
print(quote)
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"subject:motivational code\n\n{quote}")
# import smtplib
# import random
# import datetime as dt
# my_email = "debashisgoswami000@gmail.com"
# my_password = "itya nxmb zqgv mtsw"
# now = dt.datetime.now()
# weekday = now.weekday()
# with open("quotes.txt","r") as quotes_file:
#     quotes = quotes_file.readlines()
#     quote = random.choice(quotes)

# connection = smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=my_email,password=my_password)
# subject = "Motivational Code"
# message = f"Subject: {subject}\n\n{quote}"
# connection.sendmail(from_addr=my_email,to_addrs="debashisgoswami159@gmail.com",msg=message)
# connection.close()