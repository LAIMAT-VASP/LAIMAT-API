import math

def speed(g, h):

    # Paramètres de l'objet
    m = 10  # kg
    A = 0.7  # m²
    Cd = 1.0  # coefficient de traînée
    rho = 1.2  # kg/m³
    v0 = 0  # vitesse initiale de l'objet en m/s

    # Calcul de la vitesse d'impact
    v = math.sqrt((2 * m * (g * h + v0**2/2)) / (rho * A * Cd))
    v = round(v, 2)
    return v

class TestSpeed:
    def test_speed_no_height():
        assert speed(100, 0) == 0
    
    def test_speed_no_gravity():
        assert speed(0, 100) == 0
    
    def test_speed_no_gravity_no_height():
        assert speed(0, 0) == 0
    
    def test_speed_floating_height():
        assert speed(100, 100.5) == 10.025
    
    def test_speed_floating_gravity():
        assert speed(9.81, 100) == 31.62
    
    def test_speed_floating_gravity_floating_height():
        assert speed(9.81, 100.5) == 31.74
    
    def test_speed_negative_gravity():
        assert speed(-9.81, 100) == -31.62
    
    def test_speed_negative_height():
        assert speed(9.81, -100) == -31.62
    
    def test_only_gravity():
        assert speed(9.81) == 0
    
    def test_only_height():
        assert speed(height=100) == 0

def main():
    TestSpeed.test_only_gravity
    TestSpeed.test_only_height
    TestSpeed.test_speed_floating_gravity
    TestSpeed.test_speed_floating_gravity_floating_height
    TestSpeed.test_speed_floating_height
    TestSpeed.test_speed_negative_gravity
    TestSpeed.test_speed_negative_height
    TestSpeed.test_speed_no_gravity
    TestSpeed.test_speed_no_gravity_no_height
    TestSpeed.test_speed_no_height