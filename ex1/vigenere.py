def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr(((ord(char) - start + shift) % 26) + start)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr(((ord(char) - start - shift) % 26) + start)
            key_index += 1
        else:
            result += char
    return result

message = input("Enter message: ")
key_word = input("Enter key: ")

encrypted = vigenere_encrypt(message, key_word)
decrypted = vigenere_decrypt(encrypted, key_word)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
