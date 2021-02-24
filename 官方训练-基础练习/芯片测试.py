#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

n = int(input())

arr = [[] for _ in range(n)]

chip = [True for _ in range(n)]

for i in range(n):
    arr_ = input().split()
    for j in range(n):
        arr[i].append(int(arr_[j]))

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j][i] == 0:
            count += 1
    if count > n / 2:
        chip[i] = False

for i in range(n):
    if chip[i]:
        print(i + 1, end=' ')
