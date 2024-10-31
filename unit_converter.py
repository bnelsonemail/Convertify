"""
Unit Converter Base Class.

Defines the base class for the unit converter program, providing a history
tracking feature for conversions.
"""


class UnitConvert:
    """
    Base class for unit conversions.

    This class provides a structure for unit conversions and includes a
    history tracker for each conversion instance.

    Attributes
    ----------
    conversion_history : list
        A list that stores tuples of user input and output unit choices.
    """

    def __init__(self):
        """Initialize the UnitConvert class with empty conversion history."""
        self.conversion_history = []

    def question(self):
        """
        Prompt the user for additional conversions or to quit.

        If the user wishes to continue, it prompts them to choose a new
        conversion type.
        """
        question = input(
            '\nWould you like to convert something else? Type "y" for yes or '
            '"n" for no: '
        ).strip().lower()

        if question == 'y':
            from main import start_conversion
            start_conversion()
        else:
            print('\nThank you for using this application.')
