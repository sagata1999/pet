from src.structures import ImmutableTypes
from src.structures.mutable_immutable import UpperStr


class TestMutableTypes:
    def test_integer(self):
        i = ImmutableTypes()
        test_type: type[int] = i.INTEGER
        test_val: test_type = 1
        test_var = test_val
        test_var_2 = test_var
        assert id(test_var) == id(test_var_2)

        test_var += 1
        assert id(test_var_2) != id(test_var)
        assert test_var_2 != test_var


class TestUpperStr:
    def test_upper_str(self):
        s = UpperStr("hello")
        assert s == "HELLO"
