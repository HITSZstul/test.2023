def Min(a, b):
    if (a >= b):
        return b
    else:
        return a


def Select(arr1, arr2, k):
    n = len(arr1)
    m = len(arr2)
    if (k == 1):  ##若选择第一个元素，则直接返回非空数组第一个元素的较小值
        if (n == 0):
            return arr2[k-1]
        elif (m == 0):
            return arr1[k-1]
        else:
            return Min(arr1[0], arr2[0])
    elif (n == 0):  ##若有数组为空，则返回非空数组的第k个数
        return arr2[k-1]
    elif (m == 0):
        return arr1[k-1]
    else:
        if (k//2-1 >= m):  ##若有数组长度小于k//2-1，则删除的数重新讨论
            if (arr1[k//2-1] >= arr2[m-1]):  ##说明arr2中没有第k个元素值
                return arr1[k-m-1]  ##返回arr1中的第k-m个元素
            else:  ##未能确定，只能排除arr1中一半的值
                return Select(arr1[k//2:n], arr2, k-(k//2))
        elif (k//2-1 >= n):
            if (arr2[k//2-1] >= arr1[n-1]):
                return arr2[k-n-1]
            else:
                return Select(arr1, arr2[k//2:m], k-(k//2))
        else:  ##将两个数组的第k个值进行比较，将排除较大者之后的元素和较小者之前的元素
            if (arr1[k//2-1] >= arr2[k//2-1]):
                return Select(arr1, arr2[k//2:m], k-k//2)
            else:
                return Select(arr1[k//2:n], arr2, k-k//2)


n = int(input())
m = int(input())
A = []
B = []
for i in range(0, n):
    A.append(float(input()))
for i in range(0, m):
    B.append(float(input()))
sum = n + m
a = 0
if (sum % 2 == 1):
    a = Select(A, B, sum//2+1)  ##若为奇数个则返回第sum//2+1个值，为偶数则返回两个数的平均值
else:
    a = (Select(A, B, sum//2)+Select(A, B, sum//2+1))/2
print(a)
