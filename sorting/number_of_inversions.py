"""
    Count inversions in an array.
    - Inversions refer to pairs of numbers eg (a, b) where a > b.
    - Scenarios -> Compare the interests of people and recommend the friends according to the interests they share.
    Recommendations can be based on the people with the least number of conversions.
    - We shall use merge sort (nlog n) to sort the list and count the number of inversions. For example if right > left,
    that means that right is greater than all the numbers in the left array as they are sorted.
"""

count = 0
def merge_sort(arr):
    global count
    if len(arr) > 1:
        middle = len(arr)//2
        
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        
        
        while(i<len(left) and j<len(right)):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                count += (len(left)-i)
            k += 1

        while i<len(left):
            arr[k] = left[i]
            i += 1 
            k = k+1
            
        while j<len(right):
            arr[k] = right[j]
            j += 1
            k = k+1
    return count
    
def countInversions(arr):
    global count
    count = 0
    if arr == sorted(arr):
        return count
    return merge_sort(arr)

def conversion_count_naive(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

if __name__ == '__main__':
    assert countInversions([1, 1, 1, 2, 2]) == conversion_count_naive([1, 1, 1, 2, 2])
    assert countInversions([2, 1, 3, 1, 2]) == conversion_count_naive([2, 1, 3, 1, 2])
    assert countInversions([3, 2, 1]) == conversion_count_naive([3, 2, 1])