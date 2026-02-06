##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime as dt
import smtplib

my_email = "dominik.wedzina1245@gmail.com"
smtp = "smtp.gmail.com"
password = "zzopgmrdgaaptlhg"

now = dt.datetime.now()
today = now.day
current_month = now.month

data_list = pandas.read_csv("birthdays.csv").to_dict(orient="records")
for value in data_list:

    if value["month"] == current_month and value["day"] == today in data_list:
        person_name = value["name"]
        random_num = random.randint(1, 3)

        with open(f"letter_templates/letter_{random_num}.txt", mode="r") as letter_template:
            letter = letter_template.read()
            final_letter = letter.replace("[NAME]", person_name)

            with smtplib.SMTP(smtp) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="dominik.wedzina@onet.pl",
                                    msg=f"Subject:Happy Birthday {person_name}!\n\n{final_letter}")





