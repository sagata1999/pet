my_iterable = ("apple", "banana", "chuchuka")

my_iterator = iter(my_iterable)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


class Fibonacci:
    def __init__(self, max_n=None):
        self.a, self.b = 0, 1  # Первые два числа Фибоначчи
        self.max_n = max_n  # Ограничение количества чисел (если указано)
        self.count = 0  # Счётчик для ограничения итераций

    def __iter__(self):
        return self  # Итератор должен возвращать себя

    def __next__(self):
        if self.max_n is not None and self.count >= self.max_n:
            raise StopIteration  # Останавливаем итерацию, если достигли лимита

        value = self.a
        self.a, self.b = self.b, self.a + self.b  # Генерируем следующее число
        self.count += 1
        return value


f = Fibonacci()

f_iter = iter(f)
print(next(f_iter))  # 0
print(next(f_iter))  # 1
print(next(f_iter))  # 1
print(next(f_iter))  # 2
print(next(f_iter))  # 3
