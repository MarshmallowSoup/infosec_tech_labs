from functions import generate_rsa_keys, encrypt, decrypt, convert_to_numerical, numerical_to_string
import hashlib
# Define prime numbers p and q
p, q = 23, 41

# Generate RSA keys
phi_n, n, e, d = generate_rsa_keys(p, q)

# Message to be signed
message = "КП6"

# Calculate the hash of the message using SHA-256 (or any other hash function)

message_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()

# Sign the hash with the sender's private key
signature = encrypt(message_hash, n, d)

# Sender sends the message and the signature to the recipient

# Recipient's side
# Verify the signature
decrypted_signature = decrypt(signature, e, n, d)
decrypted_signature_hash = hashlib.sha256(decrypted_signature.encode('utf-8')).hexdigest()
# Calculate the hash of the received message (which should be the same as the original message)
received_message = "КП6"  # Replace with the received message
received_message_hash = hashlib.sha256(received_message.encode('utf-8')).hexdigest()

# Compare the received message's hash with the decrypted signature
if received_message_hash == decrypted_signature_hash:
    print("Message is authentic.")
else:
    print("Message is not authentic.")
