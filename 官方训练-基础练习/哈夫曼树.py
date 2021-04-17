#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

n=input()
l=list(map(int,input().split()))
s=0
for i in range(int(n)-1):
    m1=min(l)
    l.pop(l.index(m1))
    m2=min(l)
    l[l.index(m2)]=m1+m2
    s+=m1+m2
print(s)

