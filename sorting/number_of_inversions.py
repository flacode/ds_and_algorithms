"""
    Count inversions in an array.
    - Inversions refer to pairs of numbers eg (a, b) where a > b.
    - Scenarios -> Compare the interests of people and recommend the friends according to the interests they share.
    Recommendations can be based on the people with the least number of conversions.
    - We shall use merge sort (nlog n) to sort the list and count the number of inversions. For example if right > left,
    that means that right is greater than all the numbers in the left array as they are sorted.
"""

count = 0
def merge_sort(arr, start, end):
    global count
    if end-start < 2:
        return

    mid = (start+end)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)

    if arr[mid-1] <= arr[mid]: # optimization, case when the subarrays are already sorted. 
        return

    temp = []
    i = start
    j = mid
    while (i < mid and j < end):
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            count += mid - i


    while (i < mid): # optimization, only the left side needs to appended to temp, for the rest, the array is already sorted
        arr[start+len(temp)] = arr[i]
        i += 1
    
    t = 0
    while(start < end and t < len(temp)):
        arr[start] = temp[t]
        start = start + 1
        t = t + 1

    return count
    
def countInversions(arr):
    global count
    count = 0
    if arr == sorted(arr):
        return count
    return merge_sort(arr, 0, len(arr))

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