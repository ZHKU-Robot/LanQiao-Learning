##s = '0100110001010001'
s = 'aaab'
subLeng=1 #开始时 连续长度为1
count = 0
_set = set()  # 空集合，利用集合的不重复性
while subLeng <= len(s):
    _set.add(s[0:subLeng])
    # 其实像是双指针的方式
    for i in range(len(s) - subLeng):
        _set.add(s[i+1:i+subLeng+1])  
    subLeng += 1
    count += len(_set)
    print(_set)
    _set.clear()
##    每次的遍历可能有重复，所以要置空
print(count)
