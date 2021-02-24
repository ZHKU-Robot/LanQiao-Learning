#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

def A(n, k):

    if n == k:
        return

    print('sin(%d' % (n + 1), end='')

    if n + 1 != k:  # 若后边还有式子，判断是输出+号还是-号
        if n % 2 == 1:
            print('+', end='')
        else:
            print('-', end='')
    else:  # 若后边没有式子，输出右括号结束
        # 注意，这里只输出最后一次的右括号，前边左括号对应的右括号在S()函数中补全
        print(')', end='')

    n += 1

    A(n, k)  # 递归调用自身


def S(n):

    k = t = 1

    if n == 0:
        return

    for i in range(n - 1):
        print('(', end='')

    while n != 0:
        A(0, k)
        for i in range(t - 1):  # 不全A()函数中的括号
            print(')', end='')
        print('+%d' % n, end='')
        if n != 1:  # 最后一项加完整数之和不必再输出右括号
            print(')', end='')
        k += 1
        t += 1
        n -= 1


n = int(input())

# A(0, 3)

S(n)

