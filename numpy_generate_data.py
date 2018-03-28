import numpy as np

x_data = np.float32(np.random.rand(2,100))
y_data = np.dot([0.1, 0.2], x_data) + 0.300
print(y_data)