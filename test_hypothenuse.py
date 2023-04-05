import math
from hypothenuse import hypothenuse

class TestHypothenuse:
    def test_hypothenuse_positive_values(self):
        assert hypothenuse(3, 4) == 5

    def test_hypothenuse_negative_values(self):
        assert hypothenuse(-3, -4) == None

    def test_hypothenuse_zero_values(self):
        assert hypothenuse(0, 0) == 0

    def test_hypothenuse_one_value(self):
        assert hypothenuse(3, 0) == 3

    def test_hypothenuse_no_value(self):
        assert hypothenuse(0, 0) == 0

    def test_hypothenuse_float_values(self):
        assert math.isclose(hypothenuse(3.5, 5.5), 6.519202405202649)

    def test_hypothenuse_negative_float_values(self):
        assert hypothenuse(-3.5, -5.5) == None

    def test_hypothenuse_non_numeric_values(self):
        assert hypothenuse("a", "b") == None

    def test_hypothenuse_one_non_numeric_value(self):
        assert hypothenuse(3, "b") == None

    def test_hypothenuse_extreme_values(self):
        assert math.isclose(hypothenuse(10000, 10000), 14142.135623730951)

    def test_hypothenuse_negative_extreme_values(self):
        assert hypothenuse(-10000, -10000) == None

    def test_hypothenuse_equal_values(self):
        assert math.isclose(hypothenuse(3, 3), 4.242640687119285)

    def test_hypothenuse_negative_equal_values(self):
        assert hypothenuse(-3, -3) == None

    def test_hypothenuse_array_values(self):
        assert hypothenuse([3, 5], (4, 6)) == None

    def test_hypothenuse_negative_array_values(self):
        assert hypothenuse([-3, -5], (-4, -6)) == None

    def test_hypothenuse_boolean(self):
        assert hypothenuse(True, False) == None

    def test_hypothenuse_array_number(self):
        assert hypothenuse("3", "5") == None
