s=input()
upper=0
lower=0
digit=0
for i in s:
    if i.isdigit():
        digit+=1
    elif i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
print(upper,lower,digit)
