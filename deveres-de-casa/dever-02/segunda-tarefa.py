import time # Imports the time module, which will be used to measure execution time

# Defines a function called 'factorial' that receives a number 'n'
def factorial(n):
    if n == 1: 
        return n # Returns 1 (since 1! = 1)
    else:
        return n * factorial(n - 1) # Recursive case: n! = n * (n - 1)! 
    
# -- Tests -- 
if __name__ == '__main__':
    values = [10, 100, 500] # List of values used to test the factorial calculation

    for value in values:
        print('\n')
        # Measuring execution time

        start_time = time.perf_counter() # Records the start time (before execution)
        result = factorial(value) # Calculates the factorial of the current value

        end_time = time.perf_counter() # Records the end time (after execution)
        final_time = end_time - start_time # Calculates the total execution time

        # -- Results -- 
        print(f'Factorial ({value}): {result}')
        print(f'Execution time ({value}): {final_time:.10f} seconds.')

# -- Conclusions -- 

'''
O código implementa o cálculo do fatorial utilizando recursão. A função 'factorial(n)'
segue a definição matemática:

    . Caso base: quando 'n == 1', a função retorna 1, encerrando a recursão.
    . Caso recursivo: quando 'n > 1', a função retorna 'n * factorial(n - 1)'.

Análise Assintótica:

Cada chamada da função gera uma nova chamada recursiva com 'n - 1', até chegar ao 
caso base, o que implica em uma complexidade fatorial O(n!). Sendo assim, o número total 
de chamadas é proporcional a 'n'.

Apesar de o tempo de execução ser O(n), o valor produzido pela função cresce
fatorialmente. Isso significa que:

    . O número de operações cresce linearmente.
    . O tamanho do resultado numérico cresce fatorialmente.
'''