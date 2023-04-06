import math

def speed(gravity, height):
    if(height is None):
        height = 0

    if(gravity is None):
        gravity = 0
    
    if height is None or gravity is None:
        raise TypeError("Arguments cannot be None")
    
    if gravity < 0:
        gravity = -gravity
    
    if height < 0:
        height = -height

    if gravity == 0 or height == 0:
        return 0

    if(gravity == 0 or height == 0):
        return 0
    
    if(gravity < 0):
        gravity = gravity * -1

    if(height < 0):
        height = height * -1

    return round(math.sqrt(2 * gravity * height), 2)