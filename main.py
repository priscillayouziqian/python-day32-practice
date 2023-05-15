# import smtplib
#
# my_email = "priscillayouziqian@gmail.com"
# password = "abcd1234!"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # to secure my email connection via tls
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="yanpriscilla127@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of the email"
#     )

# # import a module, rename the module
# import datetime as dt
# # module.class
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# # count from 0, so 6 means Sunday
# print(day_of_week)
#
# data_of_birth = dt.datetime(year=1992, month=6, day=27)
# print(data_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "abcd1234!!!"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:  # if weekday is Sunday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()  # get a list of quotes
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

