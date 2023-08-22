import datetime
from datetime import timedelta
first_date = datetime.datetime(1994, 9, 21)
second_date = datetime.datetime(1995, 9, 28)


def date(first, second):

    while first < second:
        yield first
        first += timedelta(days=1)


e = date(first_date, second_date)
for i in e:
    print(f"{i.year}-{i.month}-{i.day}")
