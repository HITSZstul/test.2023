def MergeSort(i, j, arr, targe):
    k = (i+j)//2
    if (i == j):
        return -1
    elif (arr[k] < targe):
        k = MergeSort(k+1, j, arr, targe)
    elif (arr[k] > targe):
        k = MergeSort(i, k, arr, targe)
    else:
        return k
    return k


n = int(input())
target = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))


a = MergeSort(0, n, nums, target)
print(a)
