"""
Main module to run the unit converter program.

This program lets users choose between distance, temperature, and weight
conversion, prompting them for required inputs and performing conversions.
"""

from distance import Distance
from temperature import Temperature
from weight import Weight


def start_conversion():
    """
    Start the conversion process by prompting the user to choose a conversion
    type.

    Based on the user's choice, instantiate the appropriate class and call
    its main method for conversion. The user can choose to continue with
    further conversions or exit the program.
    """
    choices = {
        'distance': Distance,
        'temperature': Temperature,
        'weight': Weight
    }

    while True:
        choice = input(
            "\nPlease identify what type of unit you would like to convert "
            "(distance, temperature, or weight): "
        ).strip().lower()

        if choice in choices:
            converter = choices[choice]()
            converter.main()
            continue_choice = input(
                "\nWould you like to convert something else (y/n)? "
            ).strip().lower()
            if continue_choice != 'y':
                print('\nThank you for using this application.')
                break
        else:
            print("Invalid entry. Please choose 'distance', 'temperature', or "
                  "'weight'.")


if __name__ == "__main__":
    start_conversion()
