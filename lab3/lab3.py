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

def convert_to_numerical(gamma_key):
    alphabet_table = initialize_alphabet_table()
    return [alphabet_table.get(char, 0) for char in gamma_key]

def numerical_to_string(numbers):
    alphabet_table = initialize_alphabet_table()
    return ''.join([char for num in numbers for char, code in alphabet_table.items() if code == num])

def generate_rsa_keys(p, q):
    # Обчислення n та φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
