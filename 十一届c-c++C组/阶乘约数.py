number = 2
data = []
while number < 101:
    prime = True
    i = 2
    while i <= number ** 0.5:
        if number % i == 0:
            prime = False
            break
        else:
            i += 1

    if prime:
        data.append(number)
        number += 1
    else:
        number += 1
    print(data)
dic = {}
for i in data:
    dic[i] = 1

for i in range(2, 101):
    x = i
    for j in data:

        while x % j == 0:
            x //= j
            dic[j] += 1
    print(dic)
count = 1
for i in dic.values():
    count *= i
print(count)