"""
Main.

Main.py will run the converter files.
Spyder Editor.

Created on Wed Oct 30 01:49:44 2024
@author: BRICE NELSON
"""


from distance import Distance  # Import the subclass from distance.py
from temperature import Temperature  # Import the subclass from temperature.py
from weight import Weight  # Import the subclass from weight.py


distance = Distance()  # Create an instance of the subclass
distance.start()  # Call a method from the base class
distance.main()   # Call a method from the subclass

temperature = Temperature()  # Create an instance of the subclass
temperature.start()  # Call a method from the base class
temperature.main()  # Call a method from the subclass

weight = Weight()  # Create an instance of the subclass
weight.start()  # Call a method from the base class
weight.main()  # Call a method from the subclass
