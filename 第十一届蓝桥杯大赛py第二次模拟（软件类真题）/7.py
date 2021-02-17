n=6
start=1
l=[[0 for i in range(n) ] for j in range(n)]
col=0
row=0
max=n*n
def arrRowSet(row1,row2):
    global start,row
    direation=1 if row1-row2<0 else -1
    for i in range(row1,row2,direation):
        l[i][col]=start
        start+=1
        row+=direation
def arrColSet(col1, col2):
    global start,col
    direation=1 if col1-col2<0 else -1
    for i in range(col1, col2,direation):
        l[row][i] = start
        start += 1
        col+=direation
    col-=1
for i in range(n//2+1):
    arrColSet(i,n-i)
    arrRowSet(i+1,n-i)
    arrColSet(n-i-2,i)
    arrRowSet(n-i-1,i)
    row+=1
    col+=1
for a in l:
    print(a)
