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
    '6': 41, '7': 42, '8': 43, '9': 44
}

def initialize_alphabet_table():
    return ALPHABET_TABLE

def convert_to_numerical(text):
    alphabet_table = initialize_alphabet_table()
    return [alphabet_table.get(char, 0) for char in text]

def numerical_to_string(numbers):
    alphabet_table = initialize_alphabet_table()
    return ''.join([char for num in numbers for char, code in alphabet_table.items() if code == num])

def generate_rsa_keys(p, q):
    # Обчислення n та φ(n)
    n = p * q
    print("n =", n)
    phi_n = (p - 1) * (q - 1)
    return phi_n, n

def encrypt(text, n, phi):
    print(f'Original message:{text}')
    msg = convert_to_numerical(text)
    e = 2
    while(e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e += 1
    print("e =", e)

    encrypted_msg = [pow(char, e) % n for char in msg]
    print(f'Encrypted message: {encrypted_msg}')
    return encrypted_msg, e

def decrypt(encrypted_msg, e, n, phi):
    # Calculate the modular multiplicative inverse of e modulo phi
    d = pow(e, -1, phi)
    print("d =", d)
    print(f'Public key: {e, n}')
    print(f'Private key: {d, n}')
    
    # Decryption
    decrypted_msg_num = [pow(char, d, n) for char in encrypted_msg]
    decrypted_msg = numerical_to_string(decrypted_msg_num)
    print(f'Decrypted message: {decrypted_msg}')
    return decrypted_msg
     
msg = "ПЕНЯ15"
p, q = 23, 41

phi, n = generate_rsa_keys(p,q)

encrypted_msg, e = encrypt(msg, n, phi)
decrypted_msg = decrypt(encrypted_msg, e, n, phi)