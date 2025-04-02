import tracemalloc
from random import randint
from time import time


def partition(arr, low, high):
    # Выбираем точку опоры
    pivot = arr[high]

    # Index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # Traverse arr[low..high] and move all smaller
    # elements to the left side. Elements from low to
    # i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot after smaller elements and
    # return its position
    swap(arr, i + 1, high)
    return i + 1


# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# The QuickSort function implementation
def quick_sort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    tracemalloc.start()
    n = 100000
    arr = [randint(-n, n) for i in range(n)]
    arr2 = arr.copy()
    start = time()
    quick_sort(arr, 0, n - 1)
    end = time()
    snap = tracemalloc.take_snapshot()
    # display_top(snap, limit=10)

    print(f"Time spent: {end - start}")
    print(f"ARR len: {arr.__len__()}")
    print("\nSorted array is")

    assert sorted(arr2) == arr
