num=2019
s=''
while num:
    s+=chr(ord('a')+num%26-1).upper()
    num//=26
print(s[::-1])