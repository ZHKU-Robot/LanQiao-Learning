import datetime
start=datetime.datetime(2000,1,1)
end=datetime.datetime(2020,10,1)
run=0
delta=end-start
delta1=datetime.timedelta(1)
day=6
for i in range(delta.days+1):
    isMon=0
    if start.weekday()==0:
        isMon=1
    if start.day==1 or isMon:
        run+=2
    else:
        run += 1  # 1000米

    start+=delta1
    day+=1
print(run)

