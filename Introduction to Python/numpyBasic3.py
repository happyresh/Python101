import numpy as np

weight_lb = [150, 180, 200, 120, 170]
height_in = [60, 65, 72, 58, 68]
    
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(weight_lb[2])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[0:3])