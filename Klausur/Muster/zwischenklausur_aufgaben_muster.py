# Aufgabe 1


def create_boolean_matrix(n: int) -> list[list[bool]]:
    return [[i+j % 3 == 0 for j in range(n)] for i in range(n)]


# Aufgabe 2


def left_shift(a: list) -> None:
    for i in range(len(a) - 1):
        a[i], a[i+1] = a[i+1], a[i]


# Aufgabe 3


def deepcopy(a: list) -> list:
    r = []
    for i in a:
        if not isinstance(i, list):
            r.append(i)
        else:
            r.append(deepcopy(i))
    return r


# Aufgabe 4


def ggt(a: int, b: int) -> int:
    if b == 0:
        return a
    return ggt(b, a % b)


# Aufgabe 5


def collatz(n: int) -> int:
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3*n + 1)


# Aufgabe 6

memory = []
# In dem Memory sollen Tupel gespeichert werden, die die Form (n, fibonacci(n)) haben


def fibonacci(n: int) -> int:

    global memory
    # keine gute Praxis, aber macht einem an dieser Stelle das Leben leichter;
    # normal verwendet man fuer Memories keine Listen, aber ihr habt noch keine Dictionaries behandelt

    for item in memory:
        if item[0] == n:
            return item[1]

    if n <= 1:
        memory.append((n, n))
        return n

    fib = fibonacci(n-1) + fibonacci(n-2)
    memory.append((n, fib))
    return fib


# Aufgabe 7


def avg(a: list, s: int = 0, i: int = 0) -> float:
    if 0 == len(a):
        return 0
    elif i == len(a):
        return s / i
    else:
        return avg(a, s+a[i], i+1)

# Aufgabe 8


def len_recursive(a: list, i: int = 0):
    if a == []:  # alternativ auch if not a
        return i
    else:
        return len_recursive(a[1:], i + 1)


# Aufgabe 9


def count_even(a: list, i: int = 0):
    if i == len(a):
        return 0
    elif a[i] % 2 == 0:
        return 1 + count_even(a, i+1)
    else:
        return count_even(a, i+1)


# Aufgabe 10


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_prime(a: list, i: int = 0):
    if i == len(a):
        return 0
    elif is_prime(a[i]):
        return 1 + count_prime(a, i+1)
    else:
        return count_prime(a, i+1)
