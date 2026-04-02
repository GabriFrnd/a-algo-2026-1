import random
import math

# Task 1: Merge Sort
def merge_sort(array):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(array) <= 1:
        return array
    
    # Split the array into two halves
    mid = len(array) // 2
    left = merge_sort(array[:mid]) 
    right = merge_sort(array[mid:])  
    
    # Merge the sorted halves
    return merge(left, right)     

def merge(left, right):
    # Merge two sorted lists into one sorted list
    result, i, j = [], 0, 0

    # Compare elements and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Task 2: Matrix Multiplication (naive)
def matrix_multiply(A, B):
    # Assume square matrices of size n x n
    n = len(A)
    c = [[0] * n for _ in range(n)]

    # Triple nested loop for multiplication
    for i in range(n):          
        for j in range(n):      
            for k in range(n):  
                c[i][j] += A[i][k] * B[k][j]

    return c

# Task 3: Recurrences
def recurrence_a(n, memo=None):
    # Initialize memoization dictionary if needed
    if memo is None: memo = {}

    # Return cached result if available
    if n in memo: return memo[n]

    # Base case
    if n <= 1: return 1.0

    # Recursive relation: T(n) = 2T(n/4) + sqrt(n)
    memo[n] = 2 * recurrence_a(n // 4, memo) + math.sqrt(n)

    return memo[n]

def recurrence_b(n, memo=None):
    # Initialize memoization dictionary if needed
    if memo is None: memo = {}

    # Return cached result if available
    if n in memo: return memo[n]

    # Base case
    if n <= 1: return 1.0

    # Recursive relation: T(n) = 2T(n/4) + n
    memo[n] = 2 * recurrence_b(n // 4, memo) + n

    return memo[n]

def recurrence_c(n, memo=None):
    # Initialize memoization dictionary if needed
    if memo is None: memo = {}

    # Return cached result if available
    if n in memo: return memo[n]

    # Base case
    if n <= 1: return 1.0

    # Recursive relation: T(n) = 16T(n/4) + n^2
    memo[n] = 16 * recurrence_c(n // 4, memo) + n ** 2
    return memo[n]

# -- Tests --
if __name__ == '__main__':
    # Task 1: Merge Sort test with random data
    data = random.sample(range(1000), 10)
    print(f'Merge Sort: {merge_sort(data)}')

    # Task 2: Matrix Multiplication test
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print(f'Matrix Multiply: {matrix_multiply(A, B)}')

    # Task 3: Recurrences test for different n values
    for n in [1, 4, 16, 64, 256]:
        print(f'n={n:>4} | A={recurrence_a(n):>10.2f} | B={recurrence_b(n):>10.2f} | C={recurrence_c(n):>14.2f}')