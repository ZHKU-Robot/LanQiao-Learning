string=[chr(i) for i in range(ord('o'),ord('a')-1,-1)]
string[0],string[-12]=string[-12],string[0]

def bubbleSort():
    count=0    
    for i in range(len(string)):
        for j in range(len(string)-i-1):
##            print(i,j)
            if string[j+1]<string[j]:
                string[j+1],string[j]=string[j],string[j+1]
                count+=1
    print(string)        
    print(count)            
print(string)
bubbleSort()

