import structlog

from src.metaclasses.logger_mixin import LoggerMixin


class MyService(LoggerMixin):
    def greet(self, name):
        return f"Hello, {name}!"

    def add(self, x, y):
        return x + y


structlog.configure(processors=[structlog.processors.TimeStamper(fmt="iso"), structlog.processors.JSONRenderer()])


svc = MyService()
svc.greet("Alice")
svc.add(3, 5)
