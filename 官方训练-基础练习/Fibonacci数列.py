#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# def Fibonacci(n):
#     if n<=2:
#         return 1
#     else:
#         return (Fibonacci(n-1)+Fibonacci(n-2))%10007

# print(Fibonacci(int(input())))
n = int(input())
l = [1, 1]
if n <= 2:
    print(1)
else:
    for _ in range(1, n - 2):
        l += [sum(l) % 10007]
        l.pop(0)
    print(sum(l)%10007)
