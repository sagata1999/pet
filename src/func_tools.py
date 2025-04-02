from functools import reduce, lru_cache


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
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

"""
USAGE OF FILTER
"""
def lower_than_zero(num: int) -> bool:
    if num < 0:
        return True
    return False

number_list = range(-5, 5)
less_than_zero = list(filter(lower_than_zero, number_list))
print(less_than_zero)

"""
USAGE OF REDUCE
"""
# сумма умножения
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)