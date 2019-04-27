"""
    You have been given an array A of size N . you need to sort this array non-decreasing oder using bubble sort. However, you do not need to print the sorted array . You just need to print the number of swaps required to sort this array using bubble sort

    Input Format

    The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting the elements of the array.

    Output Format Print the required answer in a single line

    Constraints 1<=N<=100

"""

"""
    input(A)
        loop from last_sorted_index = len(A)-1 to 1(j)
            set swapped to False
            loop from 0 to j-1(i)
                if A[i]>A[i+1]:
                    swap(A[i], A[i+j])
                    set swapped to True
            check if swapped is not True => list is sorted
                break 

"""

def bubble_sort(A):
    count = 0
    for i in range(len(A)-1, 1, -1):
        swapped = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
                count += 1
        if not swapped:
            break
    return count


assert bubble_sort([1,2,3,4,5]) == 0
assert bubble_sort([1,3,2,4,5]) == 1