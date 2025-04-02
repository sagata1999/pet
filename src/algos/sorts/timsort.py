import tracemalloc
from random import randint
from time import time


def insertion_sort(arr, left, right):
    """Сортировка вставками для подмассива arr[left:right+1]."""
    for i in range(left + 1, right + 1):
        current = arr[i]
        j = i - 1
        while j >= left and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def merge(arr, left, mid, right):
    """Слияние двух подмассивов arr[left:mid+1] и arr[mid+1:right+1]."""
    left_copy = arr[left : mid + 1]
    right_copy = arr[mid + 1 : right + 1]
    i = j = 0
    k = left

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1

    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1


def timsort(arr):
    """Оптимизированный Timsort для списка кортежей (key, index, element)."""
    n = len(arr)
    min_run = 32

    # Сортировка мини-блоков
    for i in range(0, n, min_run):
        end = min(i + min_run - 1, n - 1)
        insertion_sort(arr, i, end)

    # Слияние блоков
    size = min_run
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(start + size - 1, n - 1)
            end = min(start + 2 * size - 1, n - 1)
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2


def sorted_with_timsort(iterable, key=None, reverse=False):
    """Аналог sorted() с использованием Timsort."""
    # Подготовка данных
    if key is None:
        key = lambda x: x  # noqa
    decorated = [(key(item), idx, item) for idx, item in enumerate(iterable)]

    # Сортировка
    timsort(decorated)

    # Применение reverse
    if reverse:
        decorated.reverse()

    # Возврат результата
    return [item[2] for item in decorated]


if __name__ == "__main__":
    n = 1000
    arr = [randint(-n, n) for i in range(n)]
    arr2 = arr.copy()
    tracemalloc.start()
    start = time()
    snap = tracemalloc.take_snapshot()
    arr = sorted_with_timsort(arr)
    snap2 = tracemalloc.take_snapshot()
    end = time()
    print(f"Time spent: {end - start}")
    print(f"ARR len: {arr.__len__()}")
    print("Sorted array:")
    stats = snap2.compare_to(snap, "lineno")

    print("Изменение памяти:")
    for stat in stats[:5]:  # Выводим топ-5 самых "тяжелых" строк кода
        print(stat)

    tracemalloc.stop()  # Останавливаем мониторинг
    assert sorted(arr2) == arr
