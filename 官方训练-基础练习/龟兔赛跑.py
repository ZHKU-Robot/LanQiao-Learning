#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

v1,v2,t,s,l=map(int,input().split())

rabbitDistance=0
turtleDistance=0

_break=0
count=0
rest=False
while rabbitDistance<l and turtleDistance<l:
    if rabbitDistance-turtleDistance>=5:
        # 开始休息
        rest=True
    if not rest:
        rabbitDistance += v1
    else:
        _break+=1
    if _break==s:
        rest=False
        _break=0

    turtleDistance+=v2
    count+=1

    print(rabbitDistance,turtleDistance)

if rabbitDistance<turtleDistance:
    print('T')
elif rabbitDistance>turtleDistance:
    print('R')
else:
    print('D')

print(count)