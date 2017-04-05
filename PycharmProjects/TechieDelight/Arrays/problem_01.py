"""
Find pair with given sum in the array
Given an unsorted array of integers, find a pair with given sum in it.

For example,

Input:
arr = [8, 7, 2, 5, 3, 1]
sum = 10

Output: 
Pair found at index 0 and 2 (8 + 2)
OR
Pair found at index 1 and 5 (7 + 3)
"""


def find_pair(int_list, int_sum):
    """ Naive Approach """

    n = len(int_list)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if int_list[i] + int_list[j] == int_sum:
                print("Pair found at index {} and {}".format(i, j))
                return

    print("Pair not found")
    return

int_list = [8, 7, 2, 5, 3, 1]
int_sum = 10

find_pair(int_list, int_sum)



