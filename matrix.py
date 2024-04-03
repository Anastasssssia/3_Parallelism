import random
import numpy as np
import os
from multiprocessing import Pool

# Функция перемножения элементов матриц
def element(index, A, B):
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    return res
# Функция для распараллеливания вычислений
def parallel_multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Количество столбцов матрицы A должно быть равно количеству строк матрицы B")
    # Создаем список индексов для каждого элемента результирующей матрицы
    indices = [(i, j) for i in range(len(A)) for j in range(len(B[0]))]

    # Определяем количество параллельных потоков
    num_threads = os.cpu_count()

    # Создаем пул процессов
    with Pool(num_threads) as pool:
        # Выполняем перемножение элементов матриц параллельно с помощью функции element
        result_elements = pool.starmap(element, [(index, A, B) for index in indices])
