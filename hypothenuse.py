import math

def hypothenuse(a, b):
    if(a is None):
        height = 0

    if(b is None):
        gravity = 0
    
    if a is None or b is None:
        raise TypeError("Arguments cannot be None")
    
    if a < 0:
        a = -a
    
    if b < 0:
        b = -b

    if a == 0 or b == 0:
        return 0

    if(a == 0 or b == 0):
        return 0
    
    if(a < 0):
        a = a * -1

    if(b < 0):
        b = b * -1
    return math.sqrt(a**2 + b**2)