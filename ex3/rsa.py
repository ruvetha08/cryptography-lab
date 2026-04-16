import math

def rsa_simple():
    print("--- Simple RSA Algorithm ---")

    p = int(input("Enter prime number p: "))  
    q = int(input("Enter prime number q: "))  
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 1
    d = pow(e, -1, phi)
    
    print(f"\nPublic Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
    msg = int(input("\nEnter a number to encrypt (less than n): "))
  
    ciphertext = pow(msg, e, n)
    print(f"Encrypted Message: {ciphertext}")
  
    decrypted_msg = pow(ciphertext, d, n)
    print(f"Decrypted Message: {decrypted_msg}")

if __name__ == "__main__":
    rsa_simple()
