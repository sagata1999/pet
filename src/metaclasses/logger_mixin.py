import structlog

logger = structlog.get_logger()


class LoggerMeta(type):
    def __new__(cls, name, bases, dct):
        orig_init = dct.get("__init__")

        # Оборачиваем методы
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith("_"):
                dct[attr_name] = cls.wrap_with_logging(attr_name, attr_value)

        # Оборачиваем __init__, чтобы добавить self.log
        def __init__(self, *args, **kwargs):  # noqa: N807
            self.log = structlog.get_logger().bind(classname=name)
            if orig_init:
                orig_init(self, *args, **kwargs)

        dct["__init__"] = __init__

        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def wrap_with_logging(method_name, method):
        def wrapper(self, *args, **kwargs):
            self.log.info("Calling method", method=method_name, args=args, kwargs=kwargs)
            result = method(self, *args, **kwargs)
            self.log.info("Method returned", method=method_name, result=result)
            return result

        return wrapper


class LoggerMixin(metaclass=LoggerMeta):
    pass
