month_3="August 2022"
from datetime import datetime

i=15

import calendar
date_for_weekday=(str(i) + " " + month_3)
print(date_for_weekday)
datetime_object = datetime.strptime(date_for_weekday, '%d %B %Y')
print(calendar.day_name[datetime_object.weekday()])