import re
k=input()
s=input()
pa="Alice|Bob(.){1,"+k+"}Bob|Alice"
print(pa)
match=re.findall(pa,s)#
print(len(match))
