#!/usr/bin/python
from datetime import datetime
now = datetime.now()
print("\033[1;42m%s/%s/%s, %s:%s:%s\033[1;m") % (now.day, now.month, now.year, now.hour, now.minute, now.second)
