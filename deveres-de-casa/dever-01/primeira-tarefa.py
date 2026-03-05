import random
import time

def insertion_sort(array):
    n = len(array)

    # An array with 1 or fewer elements is already sorted
    if n <= 1:
        return array
    
    # It iterates throught the array, starting from 1 (second element); the first one is considered sorted
    for index in range(1, n):
        key = array[index] # It stores the current element to be inserted in the sorted position
        aux = index - 1

        # It compares the current element ('key') with the elements before it
        while aux >= 0 and key < array[aux]:
            array[aux + 1] = array[aux]
            aux -= 1

        array[aux + 1] = key # Int inserts 'key' into its correct sorted position

    return array # Return of the sorted array

# --- Tests ---

if __name__ == '__main__':
    sizes = [5000, 25, 10000, 500, 75, 20000, 10, 1000, 50]
  
    for size in sizes:
        # List of random integers
        random_array = [random.randint(1, 1000) for _ in range(size)] 

        insertion_array = random_array.copy()
        sorted_array = random_array.copy()
        
        # Measuring Insertion Sort
        start_time_insertion = time.time()
        insertion_sort(insertion_array)

        end_time_insertion = time.time()
        time_insertion = end_time_insertion - start_time_insertion

        # Measuring 'sorted()'
        start_time_sorted = time.time()
        sorted(sorted_array)

        end_time_sorted = time.time()
        time_sorted = end_time_sorted - start_time_sorted

        # Results
        print('\n')
        print(f'List size: {size}')
    
        print(f'Insertion sort execution time: {time_insertion:.6f} seconds.')
        print(f'Sorted() execution time: {time_sorted:.6f} seconds.')