"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers: int):
    """Calculate preparation time.
    
    :param number_of_layers: int - number of layers the lasagna has.
    :return: int - minutes you would spend making them. Assuming each layer takes 2 minutes to prepare.

    Function takes the number of layers you want to add to the lasagna and multiplies it by the time it takes
    to make one layer.
    """
    return TIME_PER_LAYER * number_of_layers


# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate elapsed time.
    
    :param number_of_layers: int - number of layers the lasagna has.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - sum of your preparation time and the time the lasagna has already spent baking in the oven.

    Function takes the number of layers you want to add to the lasagna and the elapsed time in the oven
    and will return the sum of your preparation time and the time the lasagna has already spent baking 
    in the oven.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
    