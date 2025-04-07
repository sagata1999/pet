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


say_hello()
