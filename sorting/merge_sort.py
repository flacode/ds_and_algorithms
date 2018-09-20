"""
    1. recursively divide the list in place.
    2. end  should always be +1 the last index of the partition
"""
def merge_sort(arr, start, end):
    if end-start < 2:
        return

    mid = (start+end)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid, end)
    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
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


    while (i < mid): # optimization, only the left side needs to appended to temp, for the rest, the array is already sorted
        arr[start+len(temp)] = arr[i]
        i += 1
    
    t = 0
    while(t < len(temp)):
        arr[start] = temp[t]
        start = start + 1
        t = t + 1



if __name__ == '__main__':
    m = [7, 5, 3, 1]
    m_sorted = merge_sort(m, 0, len(m))
    assert m_sorted == [7, 5, 3, 1].sort()