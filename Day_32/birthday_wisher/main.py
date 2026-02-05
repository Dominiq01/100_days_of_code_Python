##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
# 1. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = now.day
current_month = now.month
print(today, current_month)
data = pandas.read_csv("birthdays.csv").to_dict(index=False)

for index, value in data.items():
    print(value)

# 2. If step 1 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 3. Send the letter generated in step 3 to that person's email address.




