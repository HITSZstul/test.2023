def Mid(arr):
    n = len(arr)
    if (len(arr) % 2 == 0):
        return (arr[n//2]+arr[n//2-1])/2
    else:
        return arr[n//2]


def Select(A, B):
    n = len(A)
    m = len(B)
    ptr1 = 0
    ptr2 = 0
    pre = 0
    cur = 0
    for i in range(0, (m+n)//2+1):
        pre = cur
        if (ptr1 < n and (ptr2 >= m or A[ptr1] < B[ptr2])):
            cur = A[ptr1]
            ptr1 = ptr1 + 1
        else:
            cur = B[ptr2]
            ptr2 = ptr2 + 1
    if ((m+n) % 2 == 0):
        return (pre+cur)/2
    else:
        return cur



n = int(input())
m = int(input())
A = []
B = []
for i in range(0, n):
    A.append(float(input()))
for i in range(0, m):
    B.append(float(input()))
print(Select(A, B))
