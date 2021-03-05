n=0
def dANDc(w,h):
    #基线条件是长等于宽
    global n
    if w==h:
        n+=1
        return 
    else:
        n+=1
        if w>h:
            w= w-h
        else:
            h=h-w
   
        print(w,h)
        dANDc(w,h)
dANDc(2019,324)
print(n)
