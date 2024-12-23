from typing import List, Optional


def fibonacci(n: int, memory: Optional[List[int]] = None) -> int:
    if memory is None:
        # Initialisierung des Memories, an Index n steht fibonacci(n)
        memory = [-1 for _ in range(n+1)]

    if memory[n] == -1:
        if n < 2:
            memory[n] = n
        else:
            memory[n] = fibonacci(n-1, memory) + fibonacci(n-2, memory)

    return memory[n]


def binomial_coefficient(n: int, k: int, memory: Optional[List[List[int]]] = None) -> int:
    if memory is None:
        # Memory hier als Matrix, für jedes n eine Zeile und für jedes k ein Eintrag in der Zeile
        memory = [[-1 for _ in range(k+1)] for k in range(n+1)]

    if memory[n][k] == -1:
        if k == 0 or n == k:
            memory[n][k] = 1
        else:
            memory[n][k] = binomial_coefficient(n-1, k-1, memory) + binomial_coefficient(n-1, k, memory)

    return memory[n][k]
