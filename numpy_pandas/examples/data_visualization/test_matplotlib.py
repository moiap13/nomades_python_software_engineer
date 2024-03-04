# import matplotlib.pyplot as plt

# x = ["Jan", "FEB", "MAR", "APR"]
# x1 = ["Jan", "FEB", "MAR", "APR"]
# y = [10, 20, 30, 40]
# y1 = [20, 30, 10, 80]

# plt.plot(x, y, '')
# plt.plot(x1, y1, '')
# plt.legend(["2021", "2022"])
# plt.show()

# print("hello after graph")

import numpy as np
import matplotlib.pyplot as plt


ax = plt.subplot(projection='3d')

# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()



# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 40, 50]

# plt.plot(x, y, color='green', linestyle='dashed', linewidth=2, marker='o', markerfacecolor='blue', markersize=12, label="Test")

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')

# plt.legend()

# plt.title('My first graph!')

# plt.show()

# print("End program")

# import numpy as np


# ax = plt.subplot(projection='3d')

# # Prepare arrays x, y, z
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)

# ax.plot(x, y, z, label='parametric curve')
# ax.legend()

# plt.show()

# x = ["Jan", "FEB", "MAR", "APR"]
# x1 = ["Jan", "FEB", "MAR", "APR"]
# y = [10, 20, 30, 40]
# y1 = [20, 30, 10, 80]

# plt.plot(x, y, '')
# plt.plot(x1, y1, '')
# plt.legend(["2021", "2022"])
# plt.show(block=True)

# import time
# time.sleep(5)
# print("hello")