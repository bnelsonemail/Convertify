"""
Weight.

Spyder Editor.

Created on Thu Oct 31 00:22:29 2024
@author: BRICE NELSON
"""
from unit_converter import UnitConvert


class Weight(UnitConvert):
    """
    A subclass of UnitConvert to handle weight conversions.

    This class allows users to input a weight value and convert it between
    kilograms (kg), pounds (lb), grams (g), and ounces (oz).
    """

    def main(self):
        """Handle weight conversion routing logic based on user input."""
        user_input = input(
            "\nEnter the unit you want to convert from. "
            "\nPlease choose from the following: 'kg', 'lb', 'g', or 'oz':  "
        )

        u = user_input.lower()

        if u in ['kg', 'lb', 'g', 'oz']:
            output = input(
                "\nEnter the unit you want to convert to. "
                "\nPlease choose from the following: kg, lb, g, or oz:  "
            )
            o = output.lower()
            if o not in ['kg', 'lb', 'g', 'oz']:
                print('Invalid entry, starting over.')
                self.main()
        else:
            print('Invalid entry, please try again.')
            self.main()

        user_input = u
        output = o

        # Store the conversion in the history (custom functionality)
        self.conversion_history.append((user_input, output))

        match user_input:
            case 'kg':
                if output == 'lb':
                    self.kg_to_lb(user_input, output)
                elif output == 'g':
                    self.kg_to_g(user_input, output)
                elif output == 'oz':
                    self.kg_to_oz(user_input, output)
                else:
                    self.kg_to_kg(user_input, output)
            case 'lb':
                if output == 'kg':
                    self.lb_to_kg(user_input, output)
                elif output == 'g':
                    self.lb_to_g(user_input, output)
                elif output == 'oz':
                    self.lb_to_oz(user_input, output)
                else:
                    self.lb_to_lb(user_input, output)
            case 'g':
                if output == 'kg':
                    self.g_to_kg(user_input, output)
                elif output == 'lb':
                    self.g_to_lb(user_input, output)
                elif output == 'oz':
                    self.g_to_oz(user_input, output)
                else:
                    self.g_to_g(user_input, output)
            case 'oz':
                if output == 'kg':
                    self.oz_to_kg(user_input, output)
                elif output == 'lb':
                    self.oz_to_lb(user_input, output)
                elif output == 'g':
                    self.oz_to_g(user_input, output)
                else:
                    self.oz_to_oz(user_input, output)

    # ******************** Convert from Kilograms ***************************

    def kg_to_lb(self, user_input, output):
        """Convert kilograms to pounds."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight * 2.20462
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def kg_to_g(self, user_input, output):
        """Convert kilograms to grams."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight * 1000
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def kg_to_oz(self, user_input, output):
        """Convert kilograms to ounces."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight * 35.274
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def kg_to_kg(self, user_input, output):
        """Convert kilograms to kilograms."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{weight:,.2f} {output}.")
        self.question()

    # ********************** Convert from Pounds *****************************

    def lb_to_kg(self, user_input, output):
        """Convert pounds to kilograms."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight / 2.20462
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def lb_to_g(self, user_input, output):
        """Convert pounds to grams."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight * 453.592
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def lb_to_oz(self, user_input, output):
        """Convert pounds to ounces."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight * 16
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def lb_to_lb(self, user_input, output):
        """Convert pounds to pounds."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{weight:,.2f} {output}.")
        self.question()

    # ******************* Convert from Grams ********************************

    def g_to_kg(self, user_input, output):
        """Convert grams to kilograms."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight / 1000
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def g_to_lb(self, user_input, output):
        """Convert grams to pounds."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight / 453.592
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def g_to_oz(self, user_input, output):
        """Convert grams to ounces."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight / 28.3495
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def g_to_g(self, user_input, output):
        """Convert grams to grams."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{weight:,.2f} {output}.")
        self.question()

    # ********************** Convert From Ounces ***************************

    def oz_to_kg(self, user_input, output):
        """Convert ounces to kilograms."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight / 35.274
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def oz_to_lb(self, user_input, output):
        """Convert ounces to pounds."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight / 16
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def oz_to_g(self, user_input, output):
        """Convert ounces to grams."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        result = weight * 28.3495
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{result:,.2f} {output}.")
        self.question()

    def oz_to_oz(self, user_input, output):
        """Convert ounces to ounces."""
        weight = float(input(
            '\nEnter the weight you would like to have converted: '
        ))
        print(f"\nTo convert {weight} {user_input}, the equivalent is "
              f"{weight:,.2f} {output}.")
        self.question()
