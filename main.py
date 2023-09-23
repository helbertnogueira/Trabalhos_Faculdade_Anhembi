import time
import multiprocessing

# Função para calcular a série de Fibonacci de forma sequencial
def fibonacci_sequencia(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequencia = [0, 1]
    while len(fib_sequencia) < n:
        next_value = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(next_value)
    return fib_sequencia

# Função para calcular a série de Fibonacci de forma paralela
def fibonacci_paralelos(n, num_processes):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Divide o trabalho em partes iguais para cada processo
    chunk_size = n // num_processes
    pool = multiprocessing.Pool(processes=num_processes)
    result = pool.map(fibonacci_sequencia, [chunk_size] * num_processes)

    # Combina os resultados dos processos em uma única lista
    fib_sequencia = [0, 1]
    while len(fib_sequencia) < n:
        next_values = [seq.pop() for seq in result if seq]
        next_value = sum(next_values)
        fib_sequencia.append(next_value)

    return fib_sequencia

if __name__ == "__main__":
    n = 10000  # O número de termos da série de Fibonacci a serem calculados
    num_processes = 10  # O número de processos paralelos a serem usados

    # Calcula a série de Fibonacci de forma sequencial
    start_time = time.time()
    result_seq = fibonacci_sequencia(n)
    sequential_time = time.time() - start_time

    # Calcula a série de Fibonacci de forma paralela
    start_time = time.time()
    result_parallel = fibonacci_paralelos(n, num_processes)
    parallel_time = time.time() - start_time

    print(f"Sequencial: {sequential_time} segundos")
    print(f"Paralelo ({num_processes} processos): {parallel_time} segundos")
