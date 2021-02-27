#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


n=int(input())
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
    
    t=[]
    pyramid.append(list(map(int,input().split())))
print(pyramid)
start=0
curIndex=0
leftStep=0
rightStep=0
for row in pyramid:
    #从第一行开始，逐个向下找
    for index,num in enumerate(row):
        left=0
        right=0
        if index==curIndex:#最近的左边的数
            left=num
            if index<len(row)-1:
                right=row[index+1]
            
            print("left={} right={}".format(left,right))
            print("index={},curindex={}".format(index,curIndex))
            print("leftstep={} rightstep={}".format(leftStep,rightStep))
            if leftStep==rightStep+1: #此时不能向左走了，必须向右走
                rightStep+=1
                start+=right
                curIndex=index+1
            elif leftStep+1==rightStep: #此时不能向右走了，必须向左走
                leftStep+=1
                start+=left
                curIndex=index
            else: #如果leftstep=rightstep 相等的话 选择较大的走
                if left>right:
                    leftStep+=1
                    start+=left
                    curIndex=index
                else:
                    rightStep+=1
                    start+=right
                    curIndex=index+1
            print("count=",start)
            break
        
print(start)

