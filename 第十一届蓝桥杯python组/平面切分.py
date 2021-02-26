#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


lines=[]
point=set()

class line():
    def __init__(self, a, b):
        self.b = b
        self.a = a
def findThePointOfIntersection(n):
    f=1
    for i in range(n):
        for j in range(i+1,n):
            if lines[i].a!=lines[j].a: #即斜率不一样，是平行的时候
                f=0
                x=-(lines[i].b-lines[j].b)/(lines[i].a-lines[j].b)
                y=lines[i].a*x+lines[i].b
                point.add((x,y))
                break
    if f:
        #都是平行的
        return n+1
    else:
        if len(point)==1:
            return 2*n
        else:
            return 2*n+1
n=int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    lines.append(line(a,b))
print(findThePointOfIntersection(n))
