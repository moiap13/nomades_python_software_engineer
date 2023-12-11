import time
import numpy as np

start = time.time()

array1 = [1, 2, 3, 4, 5]

for i in range(len(array1)):
    array1[i] **= 2

end = time.time()

print("For loop time:", end - start)


# function to find the square
def find_square(x):
    if x < 0:
        return 0
    else:
        return x ** 2
        
# vectorize() to vectorize the function find_square()
vectorized_function = np.vectorize(find_square)

# passing an array to a vectorized functio

start = time.time()

array1 = np.array([1, 2, 3, 4, 5 ])

result = vectorized_function(array1)

end = time.time()
print("Vectorization time:", end - start)