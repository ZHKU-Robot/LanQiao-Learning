
string=[chr(i) for i in range(ord('o'),ord('a')-1,-1)]
string[0],string[-12]=string[-12],string[0]

def bubbleSort():
    count=0
    for i in range(len(string)):
        for j in range(len(string)-i-1):
##            print(i,j)
            if string[j+1]<string[j]:
                string[j+1],string[j]=string[j],string[j+1]
                count+=1
    print(string)
    print(count)
print(string)
bubbleSort()
#

# s='ABC'
# l=list(s)
# set_=set()
# def rec(index):
#     # 如果指针已经到了交换的指针结尾
#     if(index==len(l)-1):
#         return
#     # 否则从当前交换的指针 往后 逐一递归交换
#     for i in range(index,len(l)):
#         # 第一层递归 从 0开始 交换 0,0
#         # 第二次 递归 从 1 交换 1,1
#         # 以此类推 2,1
#         print(f'第{index}层递归,交换的是{i}和{index} 还有{len(l)-i}层需要递归')
#         l[i],l[index]=l[index],l[i]
#         # print(l,i,index)
#         # 交换的加入set
#         set_.add(''.join(l))
#         #当前的状态还需要递归 获取交换后的全排列
#         rec(index+1)
#         # backtrack ~
#         l[i], l[index] = l[index], l[i]
# rec(0)
# print(set_)
