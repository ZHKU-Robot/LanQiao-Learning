nums=input()
s=''
i=0;
while i<len(nums):
    if i<len(nums)-1:
        sli=int(nums[i:i+2])
    print(sli)
    if sli<=26:
        s+=chr(ord('A')+sli-1)
        i+=2
    else:
        s+=chr(ord('A')+int(i))
        i+=1
print(s)
