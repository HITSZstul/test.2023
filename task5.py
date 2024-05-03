from collections import defaultdict
import heapq
def QuickSort(arr):
    r = len(arr)
    if (r > 1):
        x = arr[r-1]  # 选择末尾是轴枢
        j = -1
        for i in range(0, r-1):
            if (arr[i] <= x):
                j += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
        temp = arr[r-1]
        arr[r-1] = arr[j+1]
        arr[j+1] = temp
        arr[0:j+1] = QuickSort(arr[0:j+1])
        arr[j+2:r] = QuickSort(arr[j+2:r])
    return arr


num = []
n = int(input())
k = int(input())
for i in range(0, n):
    num.append(int(input()))

d = {}
for int in num:
    if int not in d.keys():
        d[int] = 1
    else:
        d[int] += 1


a = list(d.values())
a = QuickSort(a)
target = a[len(a)-k]
r = len(d)
i = 0
p = list(d.values())
q = list(d.keys())
output = []
for j in range(0, r):
    if (p[j] >= target):
        output.append(q[j])
        i += 1
    if (i == k):
        break

output = QuickSort(output)
for i in range(0, len(output)):
    print(output[i])
