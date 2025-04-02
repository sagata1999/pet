import heapq


def find_n_largest(arr, n):
    return heapq.nlargest(n, arr)

arr = [3, 1, 4, 1, 5, 9, 2, 6]
n = 3
print(find_n_largest(arr, n))
