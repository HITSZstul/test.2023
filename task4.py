def Mid(arr):
    n = len(arr)
    if (len(arr) % 2 == 0):
        return (arr[n//2]+arr[n//2-1])/2
    else:
        return arr[n//2]


def InsertSort(arr):
    for i in range(0, len(arr)-2):
        k = i
        while (arr[k] > arr[i+1]):
            k = k-1
        arr[k+1] = arr[i+1]
        for m in range(k+1, i+1):
            arr[m+1] = arr[m]


def Select(A, B):
    n = len(A)
    m = len(B)
    if (n == 0):
        return Mid(B)
    elif (m == 0):
        return Mid(A)
    else:
        a = Mid(A)
        b = Mid(B)
        k = (m+n) % 2
        if (k == 1):
            if (a < b):
                if (A[n-1] > B[m//2]):
                    return Select(A[n//2:n-1], B[0:m//2])
                else:
                    return Select(A[n//2:n], B[0:m//2-1])
            elif (a > b):
                if (A[n//2] > B[m-1]):
                    return Select(A[0:n//2-1], B[m//2:m])
                else:
                    return Select(A[0:n//2], B[m//2:m-1])
            else:
                return a
        else:
            if (a < b):
                return Select(A[n//2:n], B[0:m//2])
            elif (a > b):
                return Select(A[0:n//2], B[m//2:m])
            else:
                return a


n = int(input())
m = int(input())
A = []
B = []
for i in range(0, n):
    A.append(float(input()))
for i in range(0, m):
    B.append(float(input()))
print(Select(A, B))
