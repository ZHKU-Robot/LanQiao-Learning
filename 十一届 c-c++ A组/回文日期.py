from datetime import datetime, timedelta

date = '20200202'  # input()
year = int(date[:4])
mouth = int(date[4:6])
day = int(date[6:])
start = datetime(year, mouth, day)
print(start)

delta = timedelta(1)

palindrome = 0
ababbaba = 0

firstPalindrome=0
firstABAB=0
while (not palindrome) or (not ababbaba):
    start+=delta
    if start.month<10:
        if start.day<10:
            cur = f'{start.year}0{start.month}0{start.day}'
        else:
            cur = f'{start.year}0{start.month}{start.day}'

    else:
        if start.day < 10:
            cur = f'{start.year}{start.month}0{start.day}'
        else:
            cur = f'{start.year}{start.month}{start.day}'
    if cur==cur[::-1]:
        # 再判断是不是abab的
        if not palindrome:
            firstPalindrome=cur
        palindrome=1
        # 如果是abab 类型的,那么必然有

        if cur[0]==cur[2] and cur[1]==cur[3]:
            ababbaba=1
            firstABAB=cur
print(firstPalindrome)
print(firstABAB)
