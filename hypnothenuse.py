import math

class InvalidInputError(Exception):
    pass

def hypothenuse(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise InvalidInputError("Both inputs must be either integers or floats.")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise InvalidInputError("Boolean values are not allowed.")
    
    if a < 0 or b < 0:
        a = abs(a)
        b = abs(b)

    return math.sqrt(a**2 + b**2)

class TestHypothenuse:
    def test_hypothenuse_positive_values(self):
        assert hypothenuse(3, 4) == 5

    def test_hypothenuse_negative_values(self):
        assert hypothenuse(-3, -4) == 5

    def test_hypothenuse_zero_values(self):
        assert hypothenuse(0, 0) == 0
    
    def test_hypothenuse_one_value(self):
        assert hypothenuse(3, 0) == 3
    
    def test_hypothenuse_float_values(self):
        assert math.isclose(hypothenuse(3.5, 5.5), 6.519202405202649)

    def test_hypothenuse_negative_float_values(self):
        assert math.isclose(hypothenuse(-3.5, -5.5), 6.519202405202649)

    def test_hypothenuse_non_numeric_values(self):
        try:
            hypothenuse("a", "b")
            assert False, "Expected InvalidInputError"
        except InvalidInputError:
            pass

    def test_hypothenuse_one_non_numeric_value(self):
        try:
            hypothenuse(3, "b")
            assert False, "Expected InvalidInputError"
        except InvalidInputError:
            pass
    
    def test_hypothenuse_extreme_values(self):
        assert math.isclose(hypothenuse(10000, 10000), 14142.13562373095)

    def test_hypothenuse_negative_extreme_values(self):
        assert math.isclose(hypothenuse(-10000, -10000), 14142.13562373095)

    def test_hypothenuse_equal_values(self):
        assert math.isclose(hypothenuse(3, 3), 4.242640687119285)

    def test_hypothenuse_negative_equal_values(self):
        assert math.isclose(hypothenuse(-3, -3), 4.242640687119285)

    def test_hypothenuse_boolean(self):
        try:
            hypothenuse(True, False)
            assert False, "Expected InvalidInputError"
        except InvalidInputError:
            pass

    def test_hypothenuse_array_number(self):
        try:
            hypothenuse("3", "5")
            assert False, "Expected InvalidInputError"
        except InvalidInputError:
            pass
