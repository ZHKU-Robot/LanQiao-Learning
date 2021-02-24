#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


a = input()
b = input()
c = ""
r = 0
m = max([len(a), len(b)])
t=''.join(['0' for _ in range(abs(len(a)-len(b)))])


if len(a)>len(b):
    b=t+b
else:
    a=t+a

for i in range(- 1, -m-1, -1):
    s = sum(map(int, [a[i], b[i]]))
    c =str((s + r)%10)+c
    if s+r >= 10:
        # 产生一个进位
        r =(r+s)//10
    else:
        r = 0
    #当前位
    # print("当前和",s)
    # print("当前位",c)
    # print("进位",r)

c=str(r if r!=0 else '')+c
print((a if len(a)>len(b) else b)[:abs(len(a)-len(b))]+c)

