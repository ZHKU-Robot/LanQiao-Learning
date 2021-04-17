n=4 #int(input())

start=ord('a')
end=ord('z')
def bubbleSort(string):
    count=0
    for i in range(len(string)):
        for j in range(len(string)-i-1):
##            print(i,j)
            if string[j+1]<string[j]:
                string[j+1],string[j]=string[j],string[j+1]
                count+=1
    # print(string)
    print(count)
    return count

s='dcba'
bubbleSort(list(s))
# while 1:
#     s=[chr(i) for i in range(end,start-1,-1)]
#     if bubbleSort(s)>n:
#         end-=1
#         s = [ord(i) for i in range(end, start)]
#     else:
#         break
# print(s)





