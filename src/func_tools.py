from functools import lru_cache, reduce


def multiply(x):
    return x * x


@lru_cache(maxsize=5)  # кэшируем 5 самых частых вызовов
def add(x):
    return x + x


def skip(x):
    return x


"""
USAGE OF MAP
"""
funcs = [skip, multiply, add]
value = [lambda x: x(i) for i in range(5)]  # noqa
for i in range(5):
    value = list(map(lambda x: x(i), funcs))  # noqa
    print(value)

"""
USAGE OF FILTER
"""


def lower_than_zero(num: int) -> bool:
    return num < 0


number_list = range(-5, 5)
less_than_zero = list(filter(lower_than_zero, number_list))
print(less_than_zero)

"""
USAGE OF REDUCE
"""
# сумма умножения
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
