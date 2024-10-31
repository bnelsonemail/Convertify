"""
Main.

Main.py will run the converter files.
Spyder Editor.

Created on Wed Oct 30 01:49:44 2024
@author: BRICE NELSON
"""


from distance import Distance  # Import the subclass from distance.py
from temperature import Temperature  # Import the subclass from temperature.py


distance = Distance()  # Create an instance of the subclass
distance.start()  # Call a method from the base class
distance.main()   # Call a method from the subclass

temperature = Temperature()  # Create an instance of the subclass
temperature.start()  # Call a method from the base class
temperature.main()  # Call a method from the subclass
