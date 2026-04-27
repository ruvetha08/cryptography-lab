import hashlib
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

def generate_sha256(message):
    return hashlib.sha256(message.encode('utf-8')).hexdigest()

def generate_aes_cmac(message, key):
    key_bytes = key.encode('utf-8')
    if len(key_bytes) not in [16, 24, 32]:
        return None
    
    c = cmac.CMAC(algorithms.AES(key_bytes))
    c.update(message.encode('utf-8'))
    return c.finalize().hex()

# --- User Interaction ---

print("--- Cryptography Tool ---")
user_msg = input("Enter the message: ")
user_key = input("Enter a 16-character secret key: ")

# Generate SHA-256
sha_result = generate_sha256(user_msg)
print(f"\nSHA-256 Hash:\n{sha_result}")

# Generate CMAC
cmac_result = generate_aes_cmac(user_msg, user_key)

if cmac_result:
    print(f"\nAES-CMAC Tag:\n{cmac_result}")
else:
    print("\nError: CMAC failed. Ensure your key is exactly 16, 24, or 32 characters.")
