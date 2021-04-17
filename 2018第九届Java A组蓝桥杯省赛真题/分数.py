
def fastPower(base,exp):
    res=1

    while exp:

        if exp&1==1:
            res*=base
        base *= base
        exp>>=1
    # print(res)
    return res
def gcb(a,b):
    if b==0:
        return a
    return gcb(b,a%b)
denominator=fastPower(2,19)
molecular=0
for i in range(20):
    # print(molecular)
    molecular+=fastPower(2,i)

greatestCommonDivisor=gcb(molecular,denominator)
print(molecular,denominator,greatestCommonDivisor)