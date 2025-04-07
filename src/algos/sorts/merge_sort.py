import tracemalloc
from random import randint
from time import time


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    l = [0] * n1  # noqa
    r = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        l[i] = arr[left + i]
    for j in range(n2):
        r[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[],
    # if there are any
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        # находим центор
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    tracemalloc.start()
    n = 1000
    arr = [randint(-n, n) for i in range(n)]
    arr2 = arr.copy()
    start = time()
    merge_sort(arr, 0, len(arr) - 1)
    end = time()
    snap = tracemalloc.take_snapshot()

    print(f"Time spent: {end - start}")
    print(f"ARR len: {arr.__len__()}")
    print("\nSorted array is")

    assert sorted(arr2) == arr
