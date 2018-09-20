"""
A = [a, b,c, d]
1. index 0 is in the sorted partition
2. start at i = 1, key = A[i], compare the key with all indices greater than  or equal to 1 
3. shift A[j] and key
"""

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i
        while(j >= 1 and A[j-1] > key):
            A[j] = A[j-1]
            j = j-1
        A[j]=key

M = [6,7,7,8,8,8,7, 2,4, 5,5,6, 5,6,8,9,0,1,2,4,5]
insertion_sort(M)
print(M)

