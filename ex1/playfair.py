def encrypt_rail_fence(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0
    
    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        fence[row][col] = char
        col += 1
        row += 1 if direction_down else -1
    
    result = []
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                result.append(fence[i][j])
    return "".join(result)

def decrypt_rail_fence(cipher, rails):
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        fence[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1
                
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        if fence[row][col] != '\n':
            result.append(fence[row][col])
            col += 1
        row += 1 if direction_down else -1
    return "".join(result)

message = input("Enter message: ")
num_rails = int(input("Enter number of rails: "))

encrypted = encrypt_rail_fence(message, num_rails)
decrypted = decrypt_rail_fence(encrypted, num_rails)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
