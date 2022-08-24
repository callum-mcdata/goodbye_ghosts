"""This module does everything needed to create a delicous lasagna
"""

EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_bake_time = EXPECTED_BAKE_TIME-elapsed_bake_time

    return remaining_bake_time

def preparation_time_in_minutes(number_of_layers):
    """This function takes the number of layers that you want to add to the
    lasagna and returns how many minutes it would take to prepare them.

    :param number_of_layers = the number of layers you want to add to the lasagna
    :constant PREPERATION_TIME = the time it takes for one layer to cook
    """

    total_preparation_time = number_of_layers*PREPARATION_TIME

    return total_preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Implement the elapsed_time_in_minutes() function that has two parameters:
    :param number_of_layers = (the number of layers added to the lasagna)
    :param elapsed_bake_time = (the number of minutes the lasagna has been baking in the oven).

    This function should return the total number of minutes you've been cooking,
    or the sum of your preparation time and the time the lasagna has already
    spent baking in the oven.
    """

    total_preparation_time = preparation_time_in_minutes(number_of_layers)

    total_elapsed_time =  total_preparation_time + elapsed_bake_time

    return total_elapsed_time
