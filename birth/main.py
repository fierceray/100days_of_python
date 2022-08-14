##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime
import random
import smtplib

MY_EMAIL = "noreplyinfofromray@yahoo.com"

# TODO 1. Update the birthdays.csv DONE

# TODO 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
today = datetime.datetime.now()
filt1 = df["year"] == today.year
filt2 = df["month"] == today.month
filt3 = df["day"] == today.day
ds = df.loc[(filt1 & filt2 & filt3)]
print(ds)

# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if 0 < len(ds):
    f = random.randint(1, 3)
    for each in ds.to_records():
        print(each["name"])
        with open(f"letter_templates/letter_{f}.txt", "r") as file:
            msg = ''
            for every in file.readlines():
                msg += every.replace("[NAME]", each["name"])
            print(msg)

# TODO 4. Send the letter generated in step 3 to that person's email address.
        smtplib.SMTP.connect()
        smtplib.SMTP.login()
        smtplib.SMTP.sendmail(from_addr=MY_EMAIL,
                              to_addrs=each["email"],
                              msg=f"SUBJECT: Happy Birthdy! \n\n CONTENT: {msg}")



