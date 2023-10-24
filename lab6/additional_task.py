import sympy
import random

# Генерація великого простого числа
def generate_large_prime(n_bits):
    while True:
        candidate = random.getrandbits(n_bits)
        candidate |= (1 << n_bits - 1) | 1
        if sympy.isprime(candidate):
            return candidate

# Генерація приватного ключа
def generate_private_key():
    return random.randint(2, 100)  # Змініть діапазон за потребою

# Обчислення публічного ключа
def calculate_public_key(g, private_key, prime):
    return pow(g, private_key, prime)

# Основна функція Діффі-Хеллман обміну ключами
def diffie_hellman_key_exchange():
    # Генерація великого простого числа та генератора
    n_bits = 256  # Змініть на бажану кількість біт
    prime = generate_large_prime(n_bits)
    g = random.randint(2, prime - 1)

    # Генерація приватних ключів для Alice та Bob
    private_key_alice = generate_private_key()
    private_key_bob = generate_private_key()

    # Обчислення публічних ключів для Alice та Bob
    public_key_alice = calculate_public_key(g, private_key_alice, prime)
    public_key_bob = calculate_public_key(g, private_key_bob, prime)

    # Обмін публічними ключами (в реальній системі вони обмінювалися б через відкритий канал)

    # Обчислення спільного секретного ключа для Alice та Bob
    secret_key_alice = pow(public_key_bob, private_key_alice, prime)
    secret_key_bob = pow(public_key_alice, private_key_bob, prime)

    return prime, g, public_key_alice, public_key_bob, secret_key_alice, secret_key_bob

if __name__ == "__main__":
    prime, g, public_key_alice, public_key_bob, secret_key_alice, secret_key_bob = diffie_hellman_key_exchange()

    print(f"Велике просте число (n): {prime}")
    print(f"Генератор (g): {g}")
    print(f"Публічний ключ Alice: {public_key_alice}")
    print(f"Публічний ключ Bob: {public_key_bob}")
    print(f"Спільний секретний ключ Alice: {secret_key_alice}")
    print(f"Спільний секретний ключ Bob: {secret_key_bob}")
