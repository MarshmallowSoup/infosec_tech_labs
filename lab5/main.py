def feistel_function(left, right, round_key):
    new_left = right
    new_right = left ^ (right + round_key)
    return new_left, new_right

def pad_text(text, block_length):
    padding_length = block_length - (len(text) % block_length)
    if padding_length != block_length:
        padding = chr(padding_length)
        return text + padding * padding_length
    return text

def feistel_encrypt(plaintext, num_rounds, key):
    block_length = 2
    ciphertext = ''

    plaintext = pad_text(plaintext, block_length)

    for i in range(0, len(plaintext), block_length):
        left, right = ord(plaintext[i]), ord(plaintext[i + 1])

        for round in range(num_rounds):
            left, right = feistel_function(left, right, key)

        ciphertext += chr(left) + chr(right)

    return ciphertext

def feistel_decrypt(ciphertext, num_rounds, key):
    block_length = 2
    plaintext = ''

    for i in range(0, len(ciphertext), block_length):
        left, right = ord(ciphertext[i]), ord(ciphertext[i + 1])

        for round in range(num_rounds):
            round_key = key
            right, left = feistel_function(right, left, round_key)

        block = chr(left) + chr(right)
        plaintext += block

    return plaintext

source_text = "Hello, World!"
num_rounds = 28
key = 1

# Encrypt the source text
encrypted_text = feistel_encrypt(source_text, num_rounds, key)

# Decrypt the encrypted text
decrypted_text = feistel_decrypt(encrypted_text, num_rounds, key)

# Display the results
print("Source Text:", source_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)