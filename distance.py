"""
Distance.

A sub-class of Unit Convert.
Spyder Editor.

Created on Wed Oct 30 01:40:38 2024
@author: BRICE NELSON
"""

from unit_converter import UnitConvert


class Distance(UnitConvert):
    """Sub-class of UnitConvert, handles the distance methods."""

    def main(self):
        """
        Prompt user for the two distance units to convert.

        Evaluate user prompts to convert the units and magnitude specified.

        Args:
        ----
            km (str):   kilometer (1000 meters)
            m (str):    meter (1 / 1000 kilometers)
            cm (str):   centimeter (1 / 100 meters)
            mm (str):   millimeter (1 / 1000 meters)
            mi (str):   miles (5280 feet)
            ft (str):   feet (12 inches)
            yds (str):  yards (3 feet)
            inches (str): inches (2.54 cm)
            user_input (str)
            output(str)

        Returns
        -------
            km, m, cm, mm, mi, ft, yds, inches, output
        """
        user_input = input("\nEnter the unit you want to convert from.  "
                           "\nPlease choose from the following: "
                           "km, m, cm, mm, mi, ft, yds, or inches:  ")

        u = user_input.lower()

        if u in ['km', 'm', 'cm', 'mm', 'mi', 'ft', 'yds', 'inches']:
            output = input("\nEnter the unit you want to convert to.  "
                           "\nPlease choose from the following: "
                           "km, m, cm, mm, mi, ft, yds, or inches:  ")
            o = output.lower()
            if o in ['km', 'm', 'cm', 'mm', 'mi', 'ft', 'yds', 'inches']:
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
            case 'km':
                if output == 'mi':
                    self.km_mi(user_input, output)
                elif output == 'm':
                    self.km_m(user_input, output)
                elif output == 'cm':
                    self.km_cm(user_input, output)
                elif output == 'mm':
                    self.km_mm(user_input, output)
                elif output == 'ft':
                    self.km_ft(user_input, output)
                elif output == 'yds':
                    self.km_yds(user_input, output)
                elif output == 'inches':
                    self.km_inches(user_input, output)
                else:
                    self.km_km(user_input, output)

            case 'mi':
                if output == 'km':
                    self.mi_km(user_input, output)
                elif output == 'm':
                    self.mi_m(user_input, output)
                elif output == 'cm':
                    self.mi_cm(user_input, output)
                elif output == 'mm':
                    self.mi_mm(user_input, output)
                elif output == 'ft':
                    self.mi_ft(user_input, output)
                elif output == 'yds':
                    self.mi_yds(user_input, output)
                elif output == 'inches':
                    self.mi_inches(user_input, output)
                else:
                    self.mi_mi(user_input, output)

            case 'm':
                if output == 'km':
                    self.m_km(user_input, output)
                elif output == 'mi':
                    self.m_mi(user_input, output)
                elif output == 'cm':
                    self.m_cm(user_input, output)
                elif output == 'mm':
                    self.m_mm(user_input, output)
                elif output == 'ft':
                    self.m_ft(user_input, output)
                elif output == 'yds':
                    self.m_yds(user_input, output)
                elif output == 'inches':
                    self.m_inches(user_input, output)
                else:
                    self.m_m(user_input, output)

            case 'cm':
                if output == 'km':
                    self.cm_km(user_input, output)
                elif output == 'mi':
                    self.cm_mi(user_input, output)
                elif output == 'm':
                    self.cm_m(user_input, output)
                elif output == 'mm':
                    self.cm_mm(user_input, output)
                elif output == 'ft':
                    self.cm_ft(user_input, output)
                elif output == 'yds':
                    self.cm_yds(user_input, output)
                elif output == 'inches':
                    self.cm_inches(user_input, output)
                else:
                    self.cm_cm(user_input, output)

            case 'mm':
                if output == 'km':
                    self.mm_km(user_input, output)
                elif output == 'mi':
                    self.mm_mi(user_input, output)
                elif output == 'm':
                    self.mm_m(user_input, output)
                elif output == 'cm':
                    self.mm_cm(user_input, output)
                elif output == 'ft':
                    self.mm_ft(user_input, output)
                elif output == 'yds':
                    self.mm_yds(user_input, output)
                elif output == 'inches':
                    self.mm_inches(user_input, output)
                else:
                    self.mm_mm(user_input, output)

            case 'ft':
                if output == 'km':
                    self.ft_km(user_input, output)
                elif output == 'mi':
                    self.ft_mi(user_input, output)
                elif output == 'cm':
                    self.ft_cm(user_input, output)
                elif output == 'mm':
                    self.ft_mm(user_input, output)
                elif output == 'm':
                    self.ft_m(user_input, output)
                elif output == 'yds':
                    self.ft_yds(user_input, output)
                elif output == 'inches':
                    self.ft_inches(user_input, output)
                else:
                    self.ft_ft(user_input, output)

            case 'yds':
                if output == 'km':
                    self.yds_km(user_input, output)
                elif output == 'mi':
                    self.yds_mi(user_input, output)
                elif output == 'mi':
                    self.yds_mi(user_input, output)
                elif output == 'cm':
                    self.yds_cm(user_input, output)
                elif output == 'mm':
                    self.yds_mm(user_input, output)
                elif output == 'ft':
                    self.yds_ft(user_input, output)
                elif output == 'inches':
                    self.yds_inches(user_input, output)
                else:
                    self.yds_yds(user_input, output)

            case 'inches':
                if output == 'km':
                    self.inches_km(user_input, output)
                elif output == 'm':
                    self.inches_m(user_input, output)
                elif output == 'mi':
                    self.inches_mi(user_input, output)
                elif output == 'cm':
                    self.inches_cm(user_input, output)
                elif output == 'mm':
                    self.inches_mm(user_input, output)
                elif output == 'ft':
                    self.inches_ft(user_input, output)
                elif output == 'yds':
                    self.inches_yds(user_input, output)
                else:
                    self.inches_inches(user_input, output)

    # *************** Converting Kilometers ***************************

    def km_mi(self, user_input, output):
        """Convert kilometer to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_m(self, user_input, output):
        """Convert kilometer to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_cm(self, user_input, output):
        """Convert kilometer to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 100_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_mm(self, user_input, output):
        """Convert kilometer to millimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1_000_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_ft(self, user_input, output):
        """Convert kilometer to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1.609 * 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_yds(self, user_input, output):
        """Convert kilometer to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1.609 * (5280 / 3)
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_inches(self, user_input, output):
        """Convert kilometer to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1.609 * 5280 * 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def km_km(self, user_input, output):
        """Convert kilometer to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # ********** Converting Miles ***************************************

    def mi_km(self, user_input, output):
        """Convert miles to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_m(self, user_input, output):
        """Convert miles to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1.609 * 1000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_cm(self, user_input, output):
        """Convert miles to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1.609 * 100_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_mm(self, user_input, output):
        """Convert miles to millimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1.609 * 1_000_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_ft(self, user_input, output):
        """Convert miles to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_yds(self, user_input, output):
        """Convert miles to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 5280 / 3
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_inches(self, user_input, output):
        """Convert miles to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 5280 * 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mi_mi(self, user_input, output):
        """Convert miles to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # ***************** Converting Meters **********************************

    def m_km(self, user_input, output):
        """Convert meters to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_mi(self, user_input, output):
        """Convert meters to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1000 / 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_cm(self, user_input, output):
        """Convert meters to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 100
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_mm(self, user_input, output):
        """Convert meters to millimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 1000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_ft(self, user_input, output):
        """Convert meters to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1000 * 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_yds(self, user_input, output):
        """Convert meters to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1000 * (5280 / 3)
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_inches(self, user_input, output):
        """Convert meters to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1000 * 5280 * 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def m_m(self, user_input, output):
        """Convert meters to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # ************* Convert Centimeters ************************************

    def cm_km(self, user_input, output):
        """Convert centimeters to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 100_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_mi(self, user_input, output):
        """Convert centimeters to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / (100_000 / 1.609)
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_m(self, user_input, output):
        """Convert centimeters to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 100
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_mm(self, user_input, output):
        """Convert centimeters to millimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 10
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_ft(self, user_input, output):
        """Convert centimeters to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / (100_000 / 1.609) * 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_yds(self, user_input, output):
        """Convert centimeters to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / ((100_000 / 1.609) * 5280 / 3)
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_inches(self, user_input, output):
        """Convert centimeters to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 2.54
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def cm_cm(self, user_input, output):
        """Convert centimeters to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 2.54
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # ************* Convert Millimeters ************************************

    def mm_km(self, user_input, output):
        """Convert millimeters to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1_000_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_mi(self, user_input, output):
        """Convert millimeters to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1_000_000 / 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_m(self, user_input, output):
        """Convert millimeters to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_cm(self, user_input, output):
        """Convert millimeters to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 10
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_ft(self, user_input, output):
        """Convert millimeters to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1_000_000 / 1.609 * 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_yds(self, user_input, output):
        """Convert millimeters to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1_000_000 / 1.609 * 5280 / 3
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_inches(self, user_input, output):
        """Convert millimeters to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 1_000_000 / 1.609 * 5280 * 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def mm_mm(self, user_input, output):
        """Convert millimeters to milliimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # ********************* Convert Feet ************************************

    def ft_km(self, user_input, output):
        """Convert feet to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 5280 * 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_mi(self, user_input, output):
        """Convert feet to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_cm(self, user_input, output):
        """Convert feet to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 * 2.54
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_mm(self, user_input, output):
        """Convert feet to millimeter."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 * 2.54 * 10
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_m(self, user_input, output):
        """Convert feet to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 * 2.54 / 100
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_yds(self, user_input, output):
        """Convert feet to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 3
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_inches(self, user_input, output):
        """Convert feet to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def ft_ft(self, user_input, output):
        """Convert feet to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # *********************** Convert Yards *********************************

    def yds_km(self, user_input, output):
        """Convert yds to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 3 / 5280 * 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_mi(self, user_input, output):
        """Convert yds to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 3 / 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_m(self, user_input, output):
        """Convert yds to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 5280 * 1.609 * 1000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_cm(self, user_input, output):
        """Convert yds to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 5280 * 1.609 * 100_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_mm(self, user_input, output):
        """Convert yds to millimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 5280 * 1.609 * 1_000_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_ft(self, user_input, output):
        """Convert yds to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 3
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_inches(self, user_input, output):
        """Convert yds to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 3 * 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def yds_yds(self, user_input, output):
        """Convert yds to yards."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    # ************************ Convert Inches *******************************

    def inches_km(self, user_input, output):
        """Convert inches to kilometers."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 / 5280 * 1.609
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_mi(self, user_input, output):
        """Convert inches to miles."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 / 5280
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_m(self, user_input, output):
        """Convert inches to meters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 / 5280 * 1.609 * 1_000
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_cm(self, user_input, output):
        """Convert inches to centimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 2.54
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_mm(self, user_input, output):
        """Convert inches to millimeters."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt * 2.54 / 10
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_ft(self, user_input, output):
        """Convert inches to feet."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_yds(self, user_input, output):
        """Convert inches to yds."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt / 12 / 3
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()

    def inches_inches(self, user_input, output):
        """Convert inches to inches."""
        amt = float(input('\nEnter the distance you would like to have '
                          'converted:  '))
        result = amt
        print(f"\nTo convert {amt} {user_input}, the equivalent is "
              f"{result:,.4f} {output}.")
        self.question()
