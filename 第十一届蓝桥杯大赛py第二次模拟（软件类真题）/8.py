m = 6
n = 6

# # 暴力遍历所有 的可能
# def isValid(arr):
#     sum=0
#     for everarr in arr:
#         for arrIndex in range(1,m,2):
#             if everarr[arrIndex+1]>everarr[arrIndex] and everarr[arrIndex]<everarr[arrIndex-1]:
#                 print(''.join([str(i)+' ' for i in everarr]))
#                 sum+=1
#             else:
#                 break
#     print("sum=",sum)

l = []
flag = 0
sum=0
def generate(arr):
    global l,flag,sum

    for arrIndex in range(1,len(arr)-1):
        flag = 0
        if arr[arrIndex + 1] > arr[arrIndex] and arr[arrIndex] < arr[arrIndex - 1]:
            flag=1
        else:
            print("invalid = ",arr)
            return
    if flag:
        if len(arr)==m:
            l.append(arr)
            sum+=1
            return
    for j in range(1,n+1):
        generate(arr+[j])



generate([])
print(l)
print('sum=',sum)
