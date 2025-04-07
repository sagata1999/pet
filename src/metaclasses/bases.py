class InterfaceChecker(type):
    def __new__(cls, name, bases, _dict):
        if "save" not in _dict:
            raise TypeError(f"Класс {name} должен реализовать метод save()")
        return super().__new__(cls, name, bases, _dict)


# Работает:
class GoodClass(metaclass=InterfaceChecker):
    def save(self):
        print("saving")


# Ошибка:
class BadClass(metaclass=InterfaceChecker):
    pass


plugin_registry = {}


class PluginMeta(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if not name.startswith("Base"):  # исключим базу
            plugin_registry[name] = new_cls
        return new_cls


class BasePlugin(metaclass=PluginMeta):
    pass


class HelloPlugin(BasePlugin):
    def run(self):
        print("Hello!")


class GoodbyePlugin(BasePlugin):
    def run(self):
        print("Goodbye!")


print(plugin_registry)
