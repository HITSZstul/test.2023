def InsertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key


def Partition(arr):
    r = len(arr)
    x = arr[0]
    j = 0
    for i in range(0, r-1):
        if(arr[i] <= x):
            j += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    return arr[i]


B = []


def Select(arr, i):
    n = len(arr)
    for j in range(1, n//5):
        InsertSort(arr[(j-1)*5+1:(j-1)*5+5])
        B[j]=arr[(j-1)*5+3] ##返回插入排序后的第三个数
    x = Select(B[1:n//5],n//10)
    k = Partition(arr, x)
    if(k==i):return x
    elif(k < i):return Select(arr[1:k-1], i-k)
    else:return Select(arr[k+1:n], i)

num = []
n = int(input())
k = int(input())
for i in range(0, n):
    num.append(int(input()))
a = Partition(num)
print(num)
print(a)
