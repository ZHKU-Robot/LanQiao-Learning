#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

rect_1 = list(map(float, input().split()))

rect_2 = list(map(float, input().split()))
area = 0

x1 = max(min(rect_1[0], rect_1[2]), min(rect_2[0], rect_2[2]))

y1 = max(min(rect_1[1], rect_1[3]), min(rect_2[1], rect_2[3]))

x2 = min(max(rect_1[0], rect_1[2]), max(rect_2[0], rect_2[2]))

y2 = min(max(rect_1[1], rect_1[3]), max(rect_2[1], rect_2[3]))

if x1 < x2 and y1 < y2:
    area = (x2 - x1) * (y2 - y1)
    print('%.2f' % area)
else:
    print('%.2f' % area)