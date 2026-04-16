def get_matrix_inverse(matrix, modulus):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % modulus
    det_inv = -1
    for i in range(modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break
    if det_inv == -1:
        return None

    inv_matrix = [
        [(matrix[1][1] * det_inv) % modulus, (-matrix[0][1] * det_inv) % modulus],
        [(-matrix[1][0] * det_inv) % modulus, (matrix[0][0] * det_inv) % modulus]
    ]
    return inv_matrix

msg = input("Enter a 2-letter message (e.g., HI): ").upper()
print("Enter 4 numbers for a 2x2 key matrix:")
k1 = int(input("Row 1, Col 1: "))
k2 = int(input("Row 1, Col 2: "))
k3 = int(input("Row 2, Col 1: "))
k4 = int(input("Row 2, Col 2: "))

key = [[k1, k2], [k3, k4]]
msg_vec = [ord(msg[0]) - 65, ord(msg[1]) - 65]

enc_vec = [
    (key[0][0] * msg_vec[0] + key[0][1] * msg_vec[1]) % 26,
    (key[1][0] * msg_vec[0] + key[1][1] * msg_vec[1]) % 26
]

cipher_text = chr(enc_vec[0] + 65) + chr(enc_vec[1] + 65)
print(f"Encrypted: {cipher_text}")

inv_key = get_matrix_inverse(key, 26)
if inv_key:
    dec_vec = [
        (inv_key[0][0] * enc_vec[0] + inv_key[0][1] * enc_vec[1]) % 26,
        (inv_key[1][0] * enc_vec[0] + inv_key[1][1] * enc_vec[1]) % 26
    ]
    plain_text = chr(dec_vec[0] + 65) + chr(dec_vec[1] + 65)
    print(f"Decrypted: {plain_text}")
else:
    print("Decryption failed: Matrix is not invertible mod 26.")
