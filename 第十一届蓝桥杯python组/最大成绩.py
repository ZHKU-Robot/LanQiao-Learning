#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

start=3
n=5
# n=1
# 3

 # n=2
# 3
#4 5

# n=3
#  3
# 4 5
#6 7 8

# n-1个空格
pyramid=[]
for i in range(n):
    print(''.join([' ' for j in range(n-i-1)]),end='')
    t=[]
    for j in range(i+1):
        print(' ', end='')
        print(start,end='')
        t.append(start)
        start+=1
    pyramid.append(t)
    print()
print(pyramid)
count=3
curIndex=0
for row in pyramid[1:]:
    #从第一行开始，逐个向下找
    for index,num in enumerate(row):
        if abs(num-count)==1 and (index==curIndex or curIndex+1==index):
            count += num
            print("选中了",num,"现在的count是",count)


            curIndex=index
print(count)

