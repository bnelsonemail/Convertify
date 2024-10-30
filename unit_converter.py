"""
Unit Converter.

Spyder Editor.

Created on Mon Oct 28 22:51:20 2024
@author: BRICE NELSON

User specifies distance, weight, or temperature.  Then the user can specify
the units to convert.
"""
import sys


class UnitConvert:
    """Class to convert units of various distances, temps, and weights."""

    def __init__(self):
        """Initialize the unit converter with default values."""
        # Example attributes
        self.conversion_history = []  # To track conversion history
        # A default unit for conversions, could be anything
        self.default_unit = "km"

    def start(self):
        """
        Start the program.  Prompt the user to identify what class they.

        would like to convert, such as: distance, temperature, or weight.
        """
        menu = input("\nPlease identify what type of unit you would like "
                     "to convert, \nplease choose from the following: "
                     "distance, temperature, or weight:  ")
        print('')

        if menu.lower() == 'distance':
            # Create an instance of Distance and call its main method
            from distance import Distance
            distance = Distance()
            distance.main()

        # elif menu.lower() == 'temperature':
        #     temperature.main()

        # elif menu.lower() == 'weight':
        #     weight.main()

        else:
            print('Your entry was invalid, check your spelling and try again.')
            return self.start()

    # ************* Program Ending Logic ************************************

    def question(self):
        """Prompt user if for additional conversions or quit application."""
        question = input('\nWould you like to convert something else, type "y"'
                         ' for yes and "n" for no?  ')
        if question.lower() == 'y':
            self.start()
        else:
            print('\nThank you for using this application')
            self.exit_program()

    def exit_program(self):
        """Exit the program."""
        print("\nExiting the application.")
        sys.exit()  # Exits the application
