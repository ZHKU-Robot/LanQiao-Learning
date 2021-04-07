#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

N = 40# int(input())
martix = [[] for i in range(N)]
t = 1  # 斜着的数字
for i in range(N):
    if i%2==1:
        col = i
        row = 0
        while col >= 0 and row < N:
            martix[row].append(t)
            col -= 1
            row += 1
            t += 1
    else:
        col = 0
        row = i
        while col <=N and row >= 0:
            martix[row].append(t)
            col += 1
            row -= 1
            t += 1

for m in martix:
    print(m)
print(martix[19][19])