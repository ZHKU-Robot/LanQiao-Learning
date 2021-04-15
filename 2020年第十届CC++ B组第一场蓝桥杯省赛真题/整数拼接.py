"""
第九题：整数拼接（25分）

题目描述
给定义个长度为 n 的数组 A1,A2,⋅⋅⋅,An。你可以从中选出两个数 Ai 和 Aj ( i 不等于 j )，然后将 Ai 和 Aj 一前一后拼成一个新的整数。例如 12 和 345 可以拼成 12345 或 34512。注意交换 Ai 和 Aj 的顺序总是被视为 2 种拼法，即便是 Ai=Aj 时。
请你计算有多少种拼法满足拼出的整数是 K 的倍数。
【输入格式】
第一行包含 2 个整数 n 和 K。
第二行包含 n 个整数 A1,A2,⋅⋅⋅,An。
【输出格式】
一个整数代表答案。
【评测用例规模与约定】
对于 30% 的评测用例，1≤n≤1000,1≤K≤20,1≤Ai≤104。
对于所有评测用例，1≤n≤105，1≤K≤105，1≤Ai≤109。
————————————————
版权声明：本文为CSDN博主「元气算法」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/kiwi_berrys/article/details/111461347

"""

n,k=10,2
a=[i for i in range(1,n+1)]
print(a)
#组合数
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        t1,t2=int(str(a[i])+str(a[j])),int((str(a[i]) + str(a[j]))[::-1])
        if t1%k==0:
            count+=1
        if t2%k==0:
            count+=1
print(count)