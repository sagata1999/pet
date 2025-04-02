class TestTryExceptElseFinally:
    def finally_func(self):
        try:
            return 1 / 0
        finally:
            return 2

    def test_finally(self):
        assert self.finally_func() == 2
