from datetime import datetime, timedelta

start = datetime(1901, 1, 1)
end = datetime(2000, 12, 31)
delta = timedelta(1)
count=0
while start <= end:
    if start.weekday() == 0:
        # print(start)
        count += 1
    start+=delta
print(count)