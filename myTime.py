from datetime import datetime
from datetime import date


now = datetime.now()
#print(now)

print(now.strftime("%d- %b- %y"))
print(now.strftime("%D %B %Y %H:%M:%S "))
print(now.strftime("%A %B %d %Y %H:%M:%S"))
print(now.strftime("%a %b %d %y %H:%M %S"))
print(now.strftime("%a %b %d %Y %H:%M:%S"))
print(now.today().strftime("%a %b %d %y"))
print(date.today().strftime("%A %B %d %Y" ))