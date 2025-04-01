from time import time
from random import randint


def insertion_sort(arr):
    """
    Сортировка вставками подходит для небольших или почти отсортированных массивов
    работает за О(n^2) в среднем, лучшее время O(n) - если массив отсортирован
    по месту O(1)
    :param arr: массив для сортировки
    :return:
    """
    n = len(arr)  # длинна массива

    for i in range(1, n):  # проходимся по всему массиву
        key = arr[i]  # ключ для сортировки
        j = i - 1


        # пока второй индекс больше нуля и ключ больше чем элемент индекса
        # движемся влево и ищем подходящую позицию для ключа
        # в это время двигая все элементы вправо, на место ключа
        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    n = 10000
    arr = [randint(-n, n) for i in range(n)]
    arr2 = arr.copy()
    start = time()
    insertion_sort(arr)
    end = time()
    print(f"Time spent: {end - start}")
    print(f"ARR len: {arr.__len__()}")
    # print("Sorted array:")
    # for i in range(len(arr)):
    #     print("%d" % arr[i], end=" ")

    assert sorted(arr2) == arr