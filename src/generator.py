

class Fibonacci:
    def __init__(self, max_n=None):
        self.max_n = max_n

    def __iter__(self):
        a, b = 0, 1
        count = 0
        while self.max_n is None or count < self.max_n:
            yield a
            a, b = b, a + b
            count += 1


# Использование:
fib_gen = Fibonacci()
fib_iter = iter(fib_gen)
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))
print(next(fib_iter))


def generator1():
    yield from [1, 2, 3]


def generator2():
    yield from generator1()
    yield from [4, 5]


generator = generator2()
gen_iter = iter(generator)

print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))

try:
    next(gen_iter)
except Exception as exc:
    assert isinstance(exc, StopIteration)
