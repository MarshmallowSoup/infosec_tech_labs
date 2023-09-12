# Define the alphabet table
alphabet_table = {
    'А': '01', 'Б': '02', 'В': '03', 'Г': '04', 'Ґ': '05',
    'Д': '06', 'Е': '07', 'Є': '08', 'Ж': '09', 'З': '10',
    'И': '11', 'І': '12', 'Ї': '13', 'Й': '14', 'К': '15',
    'Л': '16', 'М': '17', 'Н': '18', 'О': '19', 'П': '20',
    'Р': '21', 'С': '22', 'Т': '23', 'У': '24', 'Ф': '25',
    'Х': '26', 'Ц': '27', 'Ч': '28', 'Ш': '29', 'Щ': '30',
    'Ь': '31', 'Ю': '32', 'Я': '33', ' ': '34', '0': '35',
    '1': '36', '2': '37', '3': '38', '4': '39', '5': '40',
    '6': '41', '7': '42', '8': '43', '9': '44'
}

# Define the gamma key
gamma_key = "БОРИМИР"

# Convert the gamma key to numerical values
gamma_numerical = [alphabet_table[letter] for letter in gamma_key]

# Message to encrypt
message = "ЧОРАПНЕМОРЕ_201"

# Initialize the encrypted message
encrypted_message = ""

# Encrypt the message using the gamma key
for i, char in enumerate(message):
    if char in alphabet_table:
        char_code = alphabet_table[char]
        gamma_code = gamma_numerical[i % len(gamma_key)]
        encrypted_char_code = (int(char_code) + int(gamma_code)) % 45  # Modulo 45 to wrap around the alphabet
        for letter, code in alphabet_table.items():
            if code == str(encrypted_char_code).zfill(2):
                encrypted_message += letter
    else:
        # If the character is not in the alphabet table, keep it unchanged
        encrypted_message += char

# Print the encrypted message
print("Encrypted Message:", encrypted_message)
