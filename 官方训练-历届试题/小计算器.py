num=0
l=[]
op=''
opDict={"ADD":"+","SUB":'-',"MUL":'*',"DIV":'/','MOD':'%'}
input()
i=0

def convert(s,toN):
    loop = '0123456789abcdefghijklmnopqrstuvwxyz'
    # 测试用例输入

    n = int(s,toN)
    a = []
    while n != 0:
        a.append( loop[i % toN] )
        n = n / toN
    a.reverse()
    out = ''.join(a)  # out:'hzqhoyh9'
    return out

print(convert('231',12))
# while 1:
#     inp=(input().split())
#     command=inp[0]
#     if len(inp)>1:
#         inpNum=inp[1]
#     if command=='CLEAR':
#         pass
#         # num=0
#     elif command=='NUM':
#         l.append(inpNum)
#         i+=1
#     elif command=='CHANGE':
#
#         pass
#     elif command=="EQUAL":
#         print(num)
#         break

# l = [22, 19, 35, 5, 3]
# for i in range(len(l)):
#     for j in range(len(l) - i - 1):
#         if l[j] > l[j + 1]:
#             l[j + 1], l[j] = l[j], l[j + 1]
#     print(l)
