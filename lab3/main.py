from functions import generate_rsa_keys, encrypt, decrypt

print("=================================================")
# task 1.2
msg = "ПЕНЯ15"
p, q = 23, 41

phi, n, e, d = generate_rsa_keys(p,q)

encrypted_msg_1 = encrypt(msg, n, e)
decrypted_msg_1 = decrypt(encrypted_msg_1, e, n, d)

# task 1.3
print("=================================================")
print("task 1.3")
print("=================================================")
encrypted_msg_2 = [258, 186, 43, 408, 633, 686, 734, 682]
decrypted_msg_2 = decrypt(encrypted_msg_2, e, n, d)
print("=================================================")
