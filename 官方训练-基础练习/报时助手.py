#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

h, m = map(int, input().split())

d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
     10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
     17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
     23: 'twenty three', 30: 'thirty', 40: 'forty', 50: 'fifty'}


if m == 0:
    print(d[h] + ' o\'clock')
else:
    print(d[h], end=' ')
    if 0 < m <= 20 or m == 30 or m == 40 or m == 50:
        print(d[m])
    elif 20 < m < 30:
        print(d[20] + ' ' + d[m - 20])
    elif 30 < m < 40:
        print(d[30] + ' ' + d[m - 30])
    elif 40 < m < 50:
        print(d[40] + ' ' + d[m - 40])
    else:
        print(d[50] + ' ' + d[m - 50])

