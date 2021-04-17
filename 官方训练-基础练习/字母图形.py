#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

letters=''.join([chr(i) for i in range(ord('A'),ord('Z')+1)])
# print(letters)
row,col=map(int ,input().split())
l=letters[:col]
for i in range(row):
    if i > 0:
        print(l[::-1][-i-1:-1],end='')
    print(l[:col-i])
