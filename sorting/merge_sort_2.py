"""
    1. merge_sort(array. start, end)
    2. if elements less than 2 ie 1, array is sorted return;
    3. find the midpoint
    4. merge_sort(lefthalf) - always start with the left.
    5. merge_sort(righthalf)
    6. merge(lefthalf, righthalf)

"""

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while(i<len(left) and j<len(right)):
            if left[i] <= right[j]: # stable sort
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i<len(left):
            arr[k] = left[i]
            i += 1 
            k = k+1
            

        while j<len(right):
            arr[k] = right[j]
            j += 1
            k = k+1

if __name__ == '__main__':
    m = [7, 5, 3, 1]
    m_sorted = merge_sort(m)
    assert m_sorted == [7, 5, 3, 1].sort()


