#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


start = [1, 1, 1]
result = 0

for i in range(20190324-4):  #
    t = 0
    for n in start:
        t += n % 10000

    start += [t]
    start.pop(0)

print(start)
result = sum(start) % 10000

print(result)
# def b(n):
#
#     if n>2:
#         ex=b(n-1)+b(n-2)+b(n-3)
#         print(ex,end=',')
#         return ex
#     else:
#         return 1
#
# b(20190324)
