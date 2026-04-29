def steps(number):

    total_steps = 0

    if number == 1:
        return total_steps

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1: 
        if number % 2 == 0:
            number = number/2
        else:
            number = (number * 3) + 1

        total_steps += 1

    return total_steps
