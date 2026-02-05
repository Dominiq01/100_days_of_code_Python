import smtplib
import datetime as dt
import random

my_email = "dominik.wedzina1245@gmail.com"
smtp = "smtp.gmail.com"
password = "zzopgmrdgaaptlhg"
now = dt.datetime.now()
year = now.year

data_of_birth = dt.datetime(year=2001 , month=8 , day=10, hour=23, minute=23)

if now.weekday() == 3:
    with open("quotes.txt") as quotes_data:
        quotes_list = quotes_data.readlines()
        random_quote = random.choice(quotes_list)

        with smtplib.SMTP(smtp) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="dominik.wedzina@onet.pl",
                                msg=f"Subject:Here is some Monday motivation!\n\n{random_quote}")
