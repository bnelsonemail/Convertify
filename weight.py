"""
Weight Conversion.

Defines the Weight subclass for converting weight units.
"""

from unit_converter import UnitConvert


class Weight(UnitConvert):
    """
    Subclass of UnitConvert for handling weight conversions.

    Converts weight between kilograms, pounds, grams, and ounces.
    """

    def main(self):
        """Prompt user for weight units and perform conversion."""
        user_input = input(
            "\nEnter the unit you want to convert from (kg, lb, g, oz): "
        ).strip().lower()

        if user_input not in ['kg', 'lb', 'g', 'oz']:
            print('Invalid entry, please try again.')
            return self.main()

        output = input(
            "Enter the unit you want to convert to (kg, lb, g, oz): "
        ).strip().lower()

        if output not in ['kg', 'lb', 'g', 'oz']:
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
            case 'kg':
                if output == 'lb':
                    self.kg_to_lb()
                elif output == 'g':
                    self.kg_to_g()
                elif output == 'oz':
                    self.kg_to_oz()
                else:
                    print("Conversion not necessary.")
                    return

    def kg_to_lb(self):
        """Convert kilograms to pounds."""
        kg = float(input('\nEnter the weight in kilograms: '))
        lb = kg * 2.20462
        print(f"{kg} kg is {lb:.2f} lb.")
