#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

input()
s=input()
n=len(s)
l=list(s)
c=f=0
m=len(l)
for i in range(m-1):
    for j in range(m-1,i-1,-1 ):
        print(i,j)
        if i==j:
            if n%2==0 or f==1:
                print("Impossible")
                exit()
            flag=1
            c+=n//2-i
        elif l[j]==l[i]: #如果找到相同字母，就要移动到相应位置
            #懂了
            for k in range(j,m-1):
                print("{} swap {}".format(l[k],l[k+1]))
                l[k],l[k+1]=l[k+1],l[k]
                print("s={}".format(''.join(l)))
                c+=1
            m-=1 #倒退一格，因为当前位置已经好了
            break
print(c)


