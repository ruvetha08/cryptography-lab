def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Apply formula
            new_char = chr(((a * (ord(char) - start) + b) % 26) + start)
            result += new_char
        else:
            result += char
    return result

def affine_decrypt(text, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Error: 'a' and 26 are not coprime. Decryption impossible."
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Apply formula
            new_char = chr(((a_inv * ((ord(char) - start) - b)) % 26) + start)
            result += new_char
        else:
            result += char
    return result

def main():
    # User Input
    message = input("Enter the message: ")
    try:
        a = int(input("Enter key 'a' (must be coprime with 26): "))
        b = int(input("Enter key 'b' (offset): "))

        if gcd(a, 26) != 1:
            print("\nError: Key 'a' must be coprime with 26.")
        else:
            encrypted = affine_encrypt(message, a, b)
            decrypted = affine_decrypt(encrypted, a, b)

            print(f"\nOriginal:  {message}")
            print(f"Encrypted: {encrypted}")
            print(f"Decrypted: {decrypted}")
            
    except ValueError:
        print("Please enter valid integers for keys a and b.")

if __name__ == "__main__":
    main()
