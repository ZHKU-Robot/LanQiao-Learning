def factorial(num:int)->int:
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
string = "LANQIAO"
leng=len(string)
print(factorial(leng)/factorial(leng-leng))

