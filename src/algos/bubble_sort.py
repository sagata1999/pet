from time import time
from random import randint
import tracemalloc
from tools.mem_control import display_top


def bubble_sort(arr):
    """
    Пузырьковая сортировка, сортирует на месте
    работает за О(n^2)
    места занимает O(1)
    :param arr: массив для сортировки
    :return:
    """
    n = len(arr)

    # Проходимся по всем элементам массива
    for i in range(n):

        # Последние i элементы уже отсортированы
        swapped = False
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

if __name__ == "__main__":
    tracemalloc.start()
    n = 1000
    arr = [randint(-n, n) for i in range(n)]
    arr2 = arr.copy()
    start = time()
    bubble_sort(arr)
    end = time()
    snap = tracemalloc.take_snapshot()
    print(f"Time spent: {end - start}")
    print(f"ARR len: {arr.__len__()}")
    print("Sorted array:")
    # for i in range(len(arr)):
    #     print("%d" % arr[i], end=" ")
    display_top(snap)
    assert sorted(arr2) == arr