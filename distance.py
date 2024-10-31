"""
Distance Conversion.

This module defines the Distance subclass for converting distance units.
"""

from unit_converter import UnitConvert


class Distance(UnitConvert):
    """
    Subclass of UnitConvert for handling distance conversions.

    Allows conversion between various units of distance.
    """

    def main(self):
        """
        Prompt the user to select units for conversion and perform the
        conversion.

        Based on user input, this method calls specific conversion methods.
        """
        user_input = input(
            "\nEnter the unit you want to convert from (km, m, cm, mm, mi, ft,"
            " yds, inches): "
        ).strip().lower()

        if user_input not in ['km', 'm', 'cm', 'mm', 'mi', 'ft', 'yds',
                              'inches']:
            print('Invalid entry, please try again.')
            return self.main()

        output = input(
            "\nEnter the unit you want to convert to (km, m, cm, mm, mi, ft, "
            "yds, inches): "
        ).strip().lower()

        if output not in ['km', 'm', 'cm', 'mm', 'mi', 'ft', 'yds', 'inches']:
            print('Invalid entry, starting over.')
            return self.main()

        self.conversion_history.append((user_input, output))

        self.route_conversion(user_input, output)

    def route_conversion(self, user_input, output):
        """
        Route the conversion to the correct method based on input and output.

        units.

        Parameters
        ----------
        user_input : str
            The unit to convert from.
        output : str
            The unit to convert to.
        """
        match user_input:
            case 'km':
                if output == 'mi':
                    self.km_to_mi()
                elif output == 'm':
                    self.km_to_m()
                elif output == 'cm':
                    self.km_to_cm()
                elif output == 'mm':
                    self.km_to_mm()
                elif output == 'ft':
                    self.km_to_ft()
                elif output == 'yds':
                    self.km_to_yds()
                elif output == 'inches':
                    self.km_to_inches()
                else:
                    print("Conversion not necessary.")
                    return

    def km_to_mi(self):
        """Convert kilometers to miles."""
        km = float(input('\nEnter the distance in kilometers: '))
        mi = km / 1.609
        print(f"{km} km is {mi:.4f} mi.")
