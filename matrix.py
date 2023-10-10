import numpy as np
import time

def matrix_multiply():
    while True:
        # Define two random matrices for multiplication
        matrix_a = np.random.rand(3, 3)
        matrix_b = np.random.rand(3, 3)

        # Perform matrix multiplication
        result = np.dot(matrix_a, matrix_b)

        # Print or process the result as needed
        print("Matrix A:")
        print(matrix_a)
        print("\nMatrix B:")
        print(matrix_b)
        print("\nResult:")
        print(result)
        print("\n---\n")

        # Introduce a delay to control the loop speed
        time.sleep(1)

# Run the matrix multiplication in an infinite loop
matrix_multiply()
