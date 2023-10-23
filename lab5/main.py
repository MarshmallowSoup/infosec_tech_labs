def feistel_network(text, rounds, shift_amount):
    def feistel_round(data, key):
        left, right = data[:len(data)//2], data[len(data)//2:]
        new_right = [0] * len(right)
        for i in range(len(right)):
            new_right[i] = (right[i] + key[i % len(key)]) % 256
        new_right = [(new_right[i] << shift_amount) % 256 for i in range(len(new_right))]
        new_left = [right[i] ^ left[i] for i in range(len(left))]
        return new_right + new_left

    data = [ord(char) for char in text]

    for _ in range(rounds):
        data = feistel_round(data, data[:len(data)//2])

    encrypted_text = ''.join(chr(byte) for byte in data)
    return encrypted_text

def decrypt_feistel(encrypted_text, rounds, shift_amount):
    def inv_shift(byte, amount):
        return (byte >> amount) % 256

    def feistel_round(data, key):
        left, right = data[:len(data)//2], data[len(data)//2:]
        new_right = [inv_shift(right[i], shift_amount) for i in range(len(right))]
        new_right = [(new_right[i] - key[i % len(key)]) % 256 for i in range(len(new_right))]
        new_left = [right[i] ^ left[i] for i in range(len(left))]
        return new_right + new_left

    data = [ord(char) for char in encrypted_text]

    for _ in range(rounds):
        data = feistel_round(data, data[:len(data)//2])

    decrypted_text = ''.join(chr(byte) for byte in data)
    return decrypted_text

# Input text to encrypt
source_text = "Hello, Feistel Network!"

# Encryption
encrypted_text = feistel_network(source_text, rounds=28, shift_amount=1)
print("Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = decrypt_feistel(encrypted_text, rounds=28, shift_amount=1)
print("Decrypted Text:", decrypted_text)
