string=input()
letters={chr(i):0 for i in range(ord('a'),ord('z'))}
for alpha in string:
    letters[alpha]+=1
key=list(letters.values()).index(max(letters.values()))
print(list(letters.keys())[key])
print(max(letters.values()))
    
         
