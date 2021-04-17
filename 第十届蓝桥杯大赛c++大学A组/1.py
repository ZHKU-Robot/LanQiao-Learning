#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

obj=['2','0','1','9']
result=[]
for i in range(1,2020):
    for num in obj:
        if num in str(i):
            result.append(i)
            break
print(result)
sum=0
for r in result:
    sum+=r**2
print(sum)