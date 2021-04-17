n = int(input())

arr = list(map(int, input().split()))

count = 0

data = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] < arr[j] < arr[k]:
                if arr[j] not in data:
                    data.append(arr[j])
                    count += 1
                # count += 1
                # arr[j] = 0

print(count)
