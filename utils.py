def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

