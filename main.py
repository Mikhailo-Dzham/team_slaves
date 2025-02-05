from utils import factorial
if __name__ == "__main__":
    n = int(input("Введіть число: "))
    print(f"Факторіал {n} = {factorial(n)}\n")

from utils import is_prime
if __name__ == "__main__":
    n = int(input("Введіть n: "))
    print(f"{n} {"не " * (not(is_prime(n)))}є простим числом")



