#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
rowList=[[1],[1,1]]
numRows=int(input())
for row in range(1, numRows - 1):
    templist = [1]
    lastrow = rowList[row]
    for colunm in range(1, len(lastrow)):
        templist.append(lastrow[colunm - 1] + lastrow[colunm])
    templist += [1]
    rowList.append(templist)
for l in rowList:
    for r in l:
        print(r,end=' ')
    print()