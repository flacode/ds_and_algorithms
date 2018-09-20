"""
    1.Calculate the appropriate gap.
    2. do i=gap to n-1
        i. key=A[i]
        ii. j = i
        iii. while(j >= gap and A[j]>key)
            a. A[j]= A[j-gap]
            b. j = j-gap
        A[j] = key
"""


def shell_sort(A):
    gap = 1
    while gap < len(A)/3:
        gap = (3*gap) + 1
        print(gap)
    while(gap >= 1):
        for i in range(gap, len(A)):
            key = A[i]
            j = i
            while(j>=gap and A[j-gap]>key):
                A[j] = A[j-gap]
                j -= gap
            A[j] = key
        gap = gap//3

    

M = [6,7,7,8,8,8,7, 2,4, 5,5,6, 5,6,8,9,0,1,2,4,5]
shell_sort(M)
print(M)

