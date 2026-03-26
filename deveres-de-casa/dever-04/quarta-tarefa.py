from math import pow # Imports the 'pow' function to calculate exponentiation.

def recursive_function(n):
    # Validation: n must be greater or equal to 1.
    if n < 1:
        raise ValueError('n must be greater or equal to 1.')
    
    print(f'Calling F({n})')

    # Base case: when F(1) = 2, returns 2.
    if n == 1:
        print(f'--> Returning 2 (base case)')
        return 2

    # Recursive calculation: F(n) = 2 * F(n - 1) + n^2.
    value = 2 * recursive_function(n - 1) * (n - 1) + pow(n, 2) 
    print(f'F({n}) = {value}')
 
    return value # Returns the computed value.

# -- Tests -- 
if __name__ == '__main__':
    try:
        # Prompts the user to enter an integer.
        n = int(input('Type an integer number: '))  
        print(f'Final result: {recursive_function(n)}.')
    except Exception:
        # Handles errors if the input is not a valid integer.
        print('Please, just type integer numbers.')