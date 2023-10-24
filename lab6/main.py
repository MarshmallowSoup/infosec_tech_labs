import sympy
import random
import time

def generate_large_prime(n_bits):
    iterations = 0
    while True:
        start_time = time.time()
        candidate = random.getrandbits(n_bits)
        candidate |= (1 << n_bits - 1) | 1
        if sympy.isprime(candidate):
            end_time = time.time()
            time_taken = end_time - start_time
            return candidate, iterations, time_taken
        iterations += 1

def find_primes_in_range(start, end):
    primes = []
    start_time = time.time()
    for num in range(start, end + 1):
        if sympy.isprime(num):
            primes.append(num)
    end_time = time.time()
    time_taken = end_time - start_time
    return primes, time_taken

def find_initial_roots(number):
    result = []
    
    start_time = time.time()
    
    for i in range(2, 101):
        root = number ** (1 / i)
        result.append(root)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return result, execution_time

# Приклади використання функцій:
if __name__ == "__main__":
    # Генерація великих простих чисел
    n = 256
    t = 10
    prime, iterations, time_taken = generate_large_prime(n)
    print("==================================================")
    print("Завдання А")
    print(f"Знайдене просте число: {prime}")
    print(f"Кількість ітерацій: {iterations}")
    print(f"Час генерації: {time_taken} секунд")
    print("==================================================")

    # Пошук простих чисел у діапазоні
    start_range = 1000
    end_range = 1100
    primes, time_taken = find_primes_in_range(start_range, end_range)
    print("Завдання Б")
    print(f"Прості числа в діапазоні: {primes}")
    print(f"Час пошуку: {time_taken} секунд")

    # Визначення перших 100 коренів числа
    number_to_find_roots = prime
    roots, time_taken = find_initial_roots(number_to_find_roots)
    print("==================================================")
    print("Завдання В")
    print(f"Перші 100 коренів числа {number_to_find_roots}: {roots}")
    print(f"Час пошуку коренів: {time_taken} секунд")
