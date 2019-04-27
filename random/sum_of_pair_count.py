"""
    Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

    Examples:
        Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
        Output :  2
        Pairs with sum 6 are (1, 5) and (7, -1)

        Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
        Output :  3
        Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         

        Input  :  arr[] = {1, 1, 1, 1}, 
                sum = 2
        Output :  6
        There are 3! pairs with sum 2.

        Input  :  arr[] = {10, 12, 10, 15, -1, 7, 6, 
                        5, 4, 2, 1, 1, 1}, 
                sum = 11
        Output :  9
        Expected time complexity O(n)
"""
from collections import defaultdict

def count_pairs(A, s):
    hash_table = defaultdict(int)
    count = 0
    for n in A:
        diff = s-n
        if hash_table.get(diff):
            count += 1*hash_table[diff]
        hash_table[n] += 1
    return count

def count_pairs_naive(A, s):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == s:
                count += 1
    return count



assert count_pairs([1, 5, 7, -1], 6) == count_pairs_naive([1, 5, 7, -1], 6)
assert count_pairs([1, 5, 7, -1, 5], 6) == count_pairs_naive([1, 5, 7, -1, 5], 6)
assert count_pairs([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11) == count_pairs_naive([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11)
assert count_pairs([1, 1, 1, 1], 2) == count_pairs_naive([1, 1, 1, 1], 2)