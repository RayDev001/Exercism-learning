import math

def score(x, y):
    # Calculate the distance from the center (0,0)
    distance = math.sqrt(x**2 + y**2)
    
    # Check the distance against the radii of the circles
    if distance <= 1:
        return 10  # Inner circle
    
    if distance <= 5:
        return 5   # Middle circle
    
    if distance <= 10:
        return 1   # Outer circle
    
    return 0   # Miss
