"""
Temperature Conversion.

Defines the Temperature subclass for converting temperature units.
"""

from unit_converter import UnitConvert


class Temperature(UnitConvert):
    """
    Subclass of UnitConvert for handling temperature conversions.

    Converts temperature between Celsius, Fahrenheit, and Kelvin.
    """

    def main(self):
        """Prompt user for temperature units and perform conversion."""
        user_input = input(
            "\nEnter the unit you want to convert from (C, F, K): "
        ).strip().upper()

        if user_input not in ['C', 'F', 'K']:
            print('Invalid entry, please try again.')
            return self.main()

        output = input(
            "Enter the unit you want to convert to (C, F, K): "
        ).strip().upper()

        if output not in ['C', 'F', 'K']:
            print('Invalid entry, starting over.')
            return self.main()
        else:
            self.route_conversion(user_input, output)

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
            case 'C':
                if output == 'F':
                    self.c_to_f()
                elif output == 'K':
                    self.c_to_k()
                else:
                    print("Conversion not necessary.")
                    return

    def c_to_f(self):
        """Convert Celsius to Fahrenheit."""
        c = float(input("\nEnter the temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c} °C is {f:.2f} °F.")
