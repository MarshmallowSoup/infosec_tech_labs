import math

ALPHABET_TABLE = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5,
    'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15,
    'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20,
    'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25,
    'Х': 26, 'Ц': 27, 'Ч': 28, 'Ш': 29, 'Щ': 30,
    'Ь': 31, 'Ю': 32, 'Я': 33, '_': 34, '0': 35,
    '1': 36, '2': 37, '3': 38, '4': 39, '5': 40,
    '6': 41, '7': 42, '8': 43, '9': 44, ' ': 45
}

def initialize_alphabet_table():
    return ALPHABET_TABLE

def convert_to_numerical(text):
    alphabet_table = initialize_alphabet_table()
    uppercase_text = text.upper()  # Convert text to uppercase
    return [alphabet_table.get(char, 0) for char in uppercase_text]

def numerical_to_string(numbers):
    # Reverse the ALPHABET_TABLE dictionary to create a mapping from numbers to characters
    reverse_alphabet_table = {value: char for char, value in ALPHABET_TABLE.items()}

    # Find the maximum value in the ALPHABET_TABLE
    max_alphabet_value = max(ALPHABET_TABLE.values())

    adjusted_numbers = [num if num <= max_alphabet_value else num % max_alphabet_value for num in numbers]

    # Use the reverse mapping to convert adjusted numbers to characters
    return ''.join([reverse_alphabet_table.get(int(num), '') for num in adjusted_numbers])


def generate_rsa_keys(p, q):
    # Обчислення n та φ(n)
    n = p * q
    print("n =", n)
    phi_n = (p - 1) * (q - 1)
    e = 2
    while(e < phi_n):
        if (math.gcd(e, phi_n) == 1):
            break
        else:
            e += 1
    print("e =", e)

    d = pow(e, -1, phi_n)
    return phi_n, n, e, d

def encrypt(text, n, e):
    print(f'Original message: {text}')
    msg = convert_to_numerical(text)

    encrypted_msg = [pow(char, e) % n for char in msg]
    print(f'Encrypted message: {encrypted_msg}')
    return encrypted_msg

def decrypt(encrypted_msg, e, n, d):
    # Calculate the modular multiplicative inverse of e modulo phi
    print("d =", d)
    print(f'Public key: {e, n}')
    print(f'Private key: {d, n}')
    
    # Decryption
    decrypted_msg_num = [pow(char, d, n) for char in encrypted_msg]
    decrypted_msg = numerical_to_string(decrypted_msg_num)
    print(f'Decrypted message: {decrypted_msg}')
    return decrypted_msg
     