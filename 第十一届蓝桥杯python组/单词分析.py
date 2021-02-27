string=input()
letters={chr(i):0 for i in range(ord('a'),ord('z'))}
print(letters)
for alpha in string:
    letters[alpha]+=1
print(letters)
print(list(letters.keys())[list(letters.values()).index(max(letters.values()))])

    
         
