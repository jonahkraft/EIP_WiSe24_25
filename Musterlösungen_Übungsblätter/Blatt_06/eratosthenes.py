def eratosthenes_iterative(n):
    nums = [True for _ in range(n)]
    nums[0] = False

    for i in range(1, n+1):
        if nums[i-1]:
            for j in range(2*i, n, i):
                nums[j-1] = False

    return [i for i in range(1, n) if nums[i-1]]


def eratosthenes_recursive(nums, current):

    # Hier mal zu Demonstrationszwecken mit einer Liste, die Zahlen enthält. Analog kann man es auch einfach
    # mit einem booleschen Array wie in der iterativen Variante machen.

    def rm_multiplies(nums, nbr, current):
        if current > max(nums):
            return
        if current in nums:
            nums.remove(current)
        rm_multiplies(nums, nbr, current+nbr)

    def sieve(nums, current, n):
        if current > n:
            return nums
        elif current == n and current in nums:
            nums.remove(current)
            return nums
        elif current > 1 and current in nums:
            rm_multiplies(nums, current, 2*current)

        return sieve(nums, current+1, n)

    if 1 in nums:
        nums.remove(1)
    return sieve(nums, current, len(nums))


print(eratosthenes_recursive(list(range(1, 101)), 1))
print(eratosthenes_iterative(100))
