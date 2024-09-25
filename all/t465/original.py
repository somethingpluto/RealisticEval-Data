# Generated with ChatGPT (modified)
from mpi4py import MPI
import numpy as np

# Function to perform matrix-vector multiplication
def matrix_vector_multiplication(matrix, vector):
    result = np.dot(matrix, vector)
    return result

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define the matrix and vector
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
vector = np.array([7, 8, 9, 10])

# Check if the matrix and vector dimensions are compatible
if matrix.shape[1] != len(vector):
    if rank == 0:
        print("Matrix and vector dimensions are not compatible for multiplication.")
elif size != matrix.shape[1]:
    print("Number of processors used doesn't match with number of rows in matrix.")
else:
    # Split the work among processes
    print(" rank: ", rank)
    local_row = comm.scatter(matrix, root=0)

    # Compute local multiplication
    local_result = matrix_vector_multiplication(local_row, vector)

    # Gather results on the root process
    global_result = comm.gather(local_result, root=0)

    # Print the result on the root process
    if rank == 0:
        print("Matrix:")
        print(matrix)
        print("Vector:")
        print(vector)
        print("Result:")
        print(global_result)
        print("Result with numpy: ")
        print( matrix@vector)