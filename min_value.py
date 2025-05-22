#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 22, 2025
# Program that uses a function to find the min value in a list

import random
import constants


# Function that returns the smallest value in a list of numbers
def find_max_value(target_list: list):
    # Initialize a variable to hold the smallest number
    current_smallest_value = target_list[0]
    # Loop through every number in the list
    for number in target_list:
        # Check if the number is smaller than the current smallest value
        if number < current_smallest_value:
            # If so, the number becomes the new current smallest value
            current_smallest_value = number
    # Return the value that survived
    return current_smallest_value


def main():
    # Initialize an empty list
    list_of_int = []

    # Fill the list up with random numbers
    for index in range(0, constants.MAX_ARRAY_SIZE):
        # Generate a random integer between MIN_NUM AND MAX_NUM
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        # Append it to the list
        list_of_int.append(random_number)
        # Display the list operation
        print(f"{random_number} added to the list at position {index}.")

    # Call find_min_value()
    smallest_value = find_max_value(list_of_int)
    # Display the min value
    print(f"\nThe min value is {smallest_value}")


if __name__ == "__main__":
    main()
