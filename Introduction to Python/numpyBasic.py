# Import the numpy package as np
"""
This script demonstrates the creation of a numpy array from a list of baseball player weights and prints the type of the resulting numpy array.
Functions:
    None
Variables:
    baseball (list): A list of baseball player weights.
    np_baseball (numpy.ndarray): A numpy array created from the baseball list.
Usage:
    Run the script to see the type of the numpy array printed to the console.
"""
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))