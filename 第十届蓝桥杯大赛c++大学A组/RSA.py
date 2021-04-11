p=891234941
q=1123984201
n=1001733993063167141
c=20190324
d=212353
for i in range(1,500000):       #枚举因子   d*e%((p-1)*(q-1))=1    (((q-1)*(p-1))*yz+1) %d =0
    if(((p-1)*(q-1)*i+1)%d==0):
        e=((p-1)*(q-1)*i+1)//212353
        print(((p-1)*(q-1)*i+1)//d) 
        break
def quick_mod(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans
x=quick_mod(c,e,n)             #x=c^e%n   579706994112328949
print(x)
print(quick_mod(x,d,n))        #c=x^d%n
