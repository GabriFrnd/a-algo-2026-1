# Defines a function called 'palindrome_recursion' that receives an array
def palindrome_recursion(array):
    # Base case: empty list or list with one element
    if len(array) <= 1:
        return True

    # Check ends
    if array[0] == array[-1]:
        return palindrome_recursion(array[1:-1]) # Calls recursively with the reduced list
    else:
        return False

# -- Tests --

if __name__ == '__main__':
    lists = [
        [0, 10, 20, 30, 20, 10, 0], 
        [25, True, 2.5, 'University', 25, False],
        ['Apple', 'Banana', 'Strawberry', 'Banana', 'Apple'],
    ]
  
    for list in lists:
        print(f'Is {list} palindrome? {palindrome_recursion(list)}.')