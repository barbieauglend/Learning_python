#python 3.5

import calendar
from datetime import date
import datetime

self = hey
priv_calendar = calendar.Calendar.monthdayscalendar(self, 2016, 11)
weekday = date.today().isocalendar()[1]

for i in range(1, 6, 30):
    print(priv_calendar)
    print(weekday)