import tracemalloc
from random import randint
from time import time


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
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    n = 1000
    arr = [randint(-n, n) for i in range(n)]
    arr2 = arr.copy()
    tracemalloc.start()
    start = time()
    snap = tracemalloc.take_snapshot()
    bubble_sort(arr)
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
