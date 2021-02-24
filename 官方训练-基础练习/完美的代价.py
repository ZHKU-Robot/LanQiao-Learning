#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

n=int(input())
s=input()
l=list(s)
c=0
for i in range(n):
    for j in range(n-i):
        l[i],l[j]=l[j],l[i]
        # print(l)
        t=''.join(l)
        print(t)
        if t==t[::-1]:
            print(t)
            print(c)
