class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Создание нового экземпляра")
            cls._instance = super().__new__(cls)
        else:
            print("Возврат уже существующего экземпляра")
        return cls._instance

    def __init__(self, value):
        print(f"Инициализация: {value}")
        self.value = value


a = Singleton("first")
print(a.value)

b = Singleton("second")
print(b.value)

print(a is b)  # True
