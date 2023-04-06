import pytest
from math import isclose

from speed import speed


class TestSpeed:
    def test_speed_floating_height(self):
        assert isclose(speed(100, 100.5), 141.77446878757826, rel_tol=1e-9)

    def test_speed_floating_gravity(self):
        assert isclose(speed(9.81, 100), 44.294469180700204, rel_tol=1e-9)

    def test_speed_floating_gravity_floating_height(self):
        assert isclose(speed(9.81, 100.5), 44.405067278408666, rel_tol=1e-9)

    def test_speed_negative_gravity(self):
        assert isclose(speed(-9.81, 100), 44.294469180700204, rel_tol=1e-9)

    def test_speed_negative_height(self):
        assert isclose(speed(9.81, -100), 0, rel_tol=1e-9)

    def test_only_gravity(self):
        with pytest.raises(TypeError):
            speed(gravity=9.81)

    def test_only_height(self):
        with pytest.raises(TypeError):
            speed(height=100)

    def test_speed_negative_gravity_negative_height(self):
        assert isclose(speed(-9.81, -100), 0, rel_tol=1e-9)

    def test_high_gravity(self):
        assert isclose(speed(999999, 100), 14142.12855266137, rel_tol=1e-9)

    def test_speed_zero_gravity(self):
        assert isclose(speed(0, 100), 0, rel_tol=1e-9)

    def test_speed_zero_height(self):
        assert isclose(speed(9.81, 0), 0, rel_tol=1e-9)

    def test_speed_zero_gravity_zero_height(self):
        assert isclose(speed(0, 0), 0, rel_tol=1e-9)

    def test_speed_none_gravity(self):
        with pytest.raises(TypeError):
            speed(None, 100)

    def test_speed_none_height(self):
        with pytest.raises(TypeError):
            speed(9.81, None)

    def test_speed_none_gravity_none_height(self):
        with pytest.raises(TypeError):
            speed(None, None)