import string

#Генерація ключа
def generate_key(keyword):
    alphabet = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя ,:.;-/")
    keyword = list(keyword.lower())

    # Use a set to track characters in the keyword for faster lookup
    keyword_set = set(keyword)

    # Add characters not in the keyword
    for char in alphabet:
        if char not in keyword_set:
            keyword.append(char)

    return ''.join(keyword)

#Функція шифрування
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char in key:
            index = key.index(char)
            encrypted_text += str(index) + ' '
        else:
            encrypted_text += char

    return encrypted_text.strip()

#Функція розшифрування
def decrypt(encrypted_text, key):
    decrypted_text = ""
    encrypted_characters = encrypted_text.split()
    for char_index in encrypted_characters:
        if char_index.isdigit():
            index = int(char_index)
            decrypted_text += key[index]
        else:
            decrypted_text += char_index

    return decrypted_text

def main():
    keyword = input("Введіть ключове слово: \n").strip()
    plaintext = input("Введіть ваш текст для шифрування: \n").lower().strip()

    key = generate_key(keyword)
    encrypted_text = encrypt(plaintext, key)

    print("Зашифрований текст: \n", encrypted_text)

    encrypted_text = input("Введіть ваш код для розшифрування: \n").lower().strip()

    decrypted_text = decrypt(encrypted_text, key)
    print("Розшифрований текст: \n", decrypted_text)

if __name__ == "__main__":
    main()