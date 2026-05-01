def equilateral(sides):
    equilateral_condition = sides[0] == sides[1] == sides[2]
    
    greater_than_zero = sides[0] > 0

    side_sum = (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])
    
    return equilateral_condition and greater_than_zero and side_sum


def isosceles(sides):
    side_0_1_equal = sides[0] == sides[1]
    side_0_2_equal = sides[0] == sides[2]
    side_1_2_equal = sides[1] == sides[2]

    isoceles_condition = side_0_1_equal or side_0_2_equal or side_1_2_equal
    
    greater_than_zero = sides[0] > 0 and sides[1] > 0 and sides[2] > 0

    side_sum = False
    if side_0_1_equal:
        side_sum = sides[0] * 2 >= sides[2]
    elif side_0_2_equal:
        side_sum = sides[0] * 2 >= sides[1]
    elif side_1_2_equal:
        side_sum = sides[1] * 2 >= sides[0]
    
    return isoceles_condition and greater_than_zero and side_sum


def scalene(sides):
    scalene_condition = sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    
    greater_than_zero = sides[0] > 0 and sides[1] > 0 and sides[2] > 0

    side_sum = (sides[0] + sides[1] >= sides[2]) and (sides[0] + sides[2] >= sides[1]) and (sides[1] + sides[2] >= sides[0])
    
    return scalene_condition and greater_than_zero and side_sum
    
