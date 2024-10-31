"""
Temperature.

Spyder Editor.

Created on Wed Oct 30 18:45:28 2024
@author: BRICE NELSON
"""
from unit_converter import UnitConvert


class Temperature(UnitConvert):
    """
    A subclass of UnitConvert to handle temperature conversions.

    This class allows users to input a temperature value and converts it
    between Celsius (C), Fahrenheit (F), and Kelvin (K). It supports the
    following conversions:

    - Celsius to Fahrenheit and Kelvin
    - Fahrenheit to Celsius and Kelvin
    - Kelvin to Celsius and Fahrenheit

    The user will be prompted to provide the temperature unit they are
    converting from, the target unit, and the temperature value. The class
    then performs the necessary conversion and outputs the result.

    Methods
    -------
    main():
        Prompts the user for input and initiates the temperature conversion.

    celsius_to_fahrenheit(celsius):
        Converts a temperature from Celsius to Fahrenheit.

    celsius_to_kelvin(celsius):
        Converts a temperature from Celsius to Kelvin.

    fahrenheit_to_celsius(fahrenheit):
        Converts a temperature from Fahrenheit to Celsius.

    fahrenheit_to_kelvin(fahrenheit):
        Converts a temperature from Fahrenheit to Kelvin.

    kelvin_to_celsius(kelvin):
        Converts a temperature from Kelvin to Celsius.

    kelvin_to_fahrenheit(kelvin):
        Converts a temperature from Kelvin to Fahrenheit.
    """

    def main(self):
        """Handle temperature conversion routing logic."""
        user_input = input("\nEnter the unit you want to convert from.  "
                           "\nPlease choose from the following: "
                           "'C', 'F', or 'K':  ")

        u = user_input.lower()

        if u in ['c', 'f', 'k']:
            output = input("\nEnter the unit you want to convert to.  "
                           "\nPlease choose from the following: "
                           "C, F, or K:  ")
            o = output.lower()
            if o in ['c', 'f', 'k']:
                pass

            else:
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

    # *************** Convert From Celsius ***********************************

    def c_f(self, user_input, output):
        """Convert Celsius to Fahrenheit."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = (temp * 9/5) + 32
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    def c_k(self, user_input, output):
        """Convert Celsius to Kelvin."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = temp + 273.15
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    def c_c(self, user_input, output):
        """Convert Celsius to Celsius."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = temp
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    # **************** Convert From Fahrenheit *******************************

    def f_c(self, user_input, output):
        """Convert Fahrenheit to Celsius."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = (temp - 32) * 5/9
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    def f_k(self, user_input, output):
        """Convert Fahrenheit to Kelvin."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = (temp - 32) * 5/9 + 273.15
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    def f_f(self, user_input, output):
        """Convert Fahrenheit to Fahrenheit."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = temp
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    # ******************** Convert From Kelvin ******************************

    def k_c(self, user_input, output):
        """Convert Kelvin to Celsius."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = temp - 273.15
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    def k_f(self, user_input, output):
        """Convert Kelvin to Fahrenheit."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = (temp - 273.15) * 9/5 + 32
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()

    def k_k(self, user_input, output):
        """Convert Kelvin to Kelvin."""
        temp = float(input('\nEnter the temperature value you would like to'
                           ' have converted:  '))
        result = temp
        user_input = user_input.upper()
        output = output.upper()
        print(f"\nTo convert {temp} degrees {user_input}, the equivalent is "
              f"{result:,.2f} degrees {output}.")
        self.question()
