filename = "some_file.txt"

# using context manager to open file, write and close
with open(filename, "w") as opened_file:
    opened_file.write("Hola!")


# эквивалент написанному выше
file = open(filename, "w")  # noqa
try:
    file.write("Hola!")
finally:
    file.close()


# Класс контекстного менеджера для файла
class File:
    exceptions = (AttributeError,)

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)  # noqa

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.exceptions:
            print(f"Exception: {exc_type} with value {exc_value} handled!")
        else:
            print("Unexpected exception happened!")
            return False

        print(f"Closing file: {self.file_obj.name}")
        self.file_obj.close()
        return True


# Пример использования
with File(filename, "w") as opened_file:
    opened_file.write("Hola!")

# Пример обработки исключения при выходе из контекстного менеджера
with File(filename, "w") as opened_file:
    opened_file.meme_method("Hola!")
