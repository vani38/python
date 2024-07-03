#datetime

import datetime
now=datetime.datetime.now()
print(now)

#date
import datetime
date=datetime.date(2024,6,15)
print(date)

#time
import datetime
time=datetime.time(12,45,30)
print(time)

#difference between dates
import datetime
date1=datetime.date(1994,8,3)
date2=datetime.date(2024,6,15)
difference=date2-date1
print("Difference:",difference)
print("Days:",difference.days)



