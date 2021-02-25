#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import datetime

start=datetime.datetime(2000,6,3)
end=datetime.datetime(2020,10,1)
run=0
delta=end-start
delta1=datetime.timedelta(1)
day=6

print(start.strftime('%a %b %d %H:%M'))
for i in range(delta.days):
    start+=delta1
    day+=1
    if start.day==1 or day%7==1:
        run+=2
        day=1
    else:
        run += 1  # 1000米
print(run)