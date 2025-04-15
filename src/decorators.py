# функция первого порядка
def apply_operation(operation, x, y):
    return operation(x, y)


def add(a, b):
    return a + b


result = apply_operation(add, 5, 3)


# частный случай функции первого порядка, декоратор
def decorator(func):
    def wrapper():
        print("Перед вызовом функции.")
        func()
        print("После вызова функции.")

    return wrapper


@decorator
def say_hello():
    print("Привет!")


def repeat(times):
    ''' вызывает функцию количество раз, равное times '''
    def decorate(fn):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = fn(*args, **kwargs)
            return result
        return wrapper
    return decorate

@repeat(5)
def cpuload(x):
    """ внутри функции cpuload ничего не изменилось """
    print(f"iter: {x}")

print(f"cpuload.__name__=={cpuload.__name__}")
print(f"CPU load is {cpuload(1)}")

say_hello()
