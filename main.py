from utils import factorial
if __name__ == "__main__":
    n = int(input("Введіть число: "))
    print(f"Факторіал {n} = {factorial(n)}\n")

from utils import is_prime
if __name__ == "__main__":
    n = int(input("Введіть n: "))
    print(f"{n} {"не " * (not(is_prime(n)))}є простим числом")


from utils import is_power_of_5
if __name__ == "__main__":
	n = int(input("Введіть число для перевірки:"))
	print(f"{"is n a power of 5? — " (is_power_of_5(n))}

