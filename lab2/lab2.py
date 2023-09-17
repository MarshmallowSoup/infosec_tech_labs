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

def convert_gamma_to_numerical(gamma_key):
    alphabet_table = initialize_alphabet_table()
    return [alphabet_table.get(char, 0) for char in gamma_key]

def numerical_to_string(numbers):
    alphabet_table = initialize_alphabet_table()
    return ''.join([char for num in numbers for char, code in alphabet_table.items() if code == num])

def encrypt(message, gamma_key):
    alphabet_table = initialize_alphabet_table()
    message_numbers = [alphabet_table.get(char, 0) for char in message]
    gamma_key_numbers = convert_gamma_to_numerical(gamma_key)

    encrypted_numbers = []
    for i, message_num in enumerate(message_numbers):
        gamma_index = i % len(gamma_key_numbers)
        sum_result = message_num + gamma_key_numbers[gamma_index]
        encrypted_number = sum_result % len(alphabet_table)

        encrypted_numbers.append(encrypted_number)

    encrypted_string = numerical_to_string(encrypted_numbers)
    return encrypted_string

def decrypt(encrypted_message, gamma_key):
    alphabet_table = initialize_alphabet_table()
    encrypted_numbers = convert_gamma_to_numerical(encrypted_message)
    gamma_key_numbers = convert_gamma_to_numerical(gamma_key)

    decrypted_numbers = []
    for i, encrypted_num in enumerate(encrypted_numbers):
        gamma_index = i % len(gamma_key_numbers)
        diff_result = encrypted_num - gamma_key_numbers[gamma_index]

        if diff_result < 0:
            diff_result += len(alphabet_table)

        decrypted_numbers.append(diff_result)

    decrypted_string = numerical_to_string(decrypted_numbers)
    return decrypted_string

def task1(gamma_key, message):
    encrypted_message = encrypt(message, gamma_key)
    
    print("Gamma key:", gamma_key)
    print("Message:", message)
    print("Encrypted Message:", encrypted_message)
    return 1
    
def task2(gamma_key, encrypted_message):
    decrypted_message = decrypt(encrypted_message, gamma_key)
    print("Gamma key:", gamma_key)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)
    return 1
def main():
    print("================================================")
    print("Завдання 1")
    task1("БОРИМИР", "ЧОРАПНЕМОРЕ_201")
    print("================================================")
    print()
    print("================================================")
    print("Завдання 2")
    task2("ДИВОЗІР", "ДЗЧЦ_РУ6ЇЗЇЕУНРЮ")
    print("================================================")

if __name__ == "__main__":
    main()
