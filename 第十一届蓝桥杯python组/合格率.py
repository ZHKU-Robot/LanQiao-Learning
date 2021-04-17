#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

n=int(input())
scores=[int(input()) for i in range(n)]
qualified=[s for s in scores if s>=60]
excellent=[s for s in scores if s>=85]
print(qualified)
print(excellent)
print('{}%'.format(round(len(qualified)/len(scores)*100)))
print('{}%'.format(round(len(excellent)/len(scores)*100)))