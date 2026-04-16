# --- TABLES & CONFIGURATION ---
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]  # Expansion Permutation
P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

# --- HELPER FUNCTIONS ---
def permute(original, table):
    return "".join(original[i - 1] for i in table)

def left_shift(bits, count):
    return bits[count:] + bits[:count]

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')

# --- KEY GENERATION ---
def generate_keys(key_10bit):
    # Step 1: P10
    p10_key = permute(key_10bit, P10)
    left, right = p10_key[:5], p10_key[5:]
    
    # Step 2: Shift & P8 -> Key 1
    left, right = left_shift(left, 1), left_shift(right, 1)
    k1 = permute(left + right, P8)
    
    # Step 3: Shift & P8 -> Key 2
    left, right = left_shift(left, 2), left_shift(right, 2)
    k2 = permute(left + right, P8)
    
    return k1, k2

# --- ENCRYPTION STEPS ---
def f_function(right_half, subkey):
    # Expand 4 bits to 8
    expanded = permute(right_half, EP)
    # XOR with Subkey
    xored = format(int(expanded, 2) ^ int(subkey, 2), '08b')
    # S-Box Substitution
    s0_out = sbox_lookup(xored[:4], S0)
    s1_out = sbox_lookup(xored[4:], S1)
    # P4 Permutation
    return permute(s0_out + s1_out, P4)

def encrypt(pt, k1, k2):
    # Initial Permutation
    state = permute(pt, IP)
    L, R = state[:4], state[4:]
    
    # Round 1
    f_res = f_function(R, k1)
    L = format(int(L, 2) ^ int(f_res, 2), '04b')
    
    # Switch (Swap L and R)
    L, R = R, L
    
    # Round 2
    f_res = f_function(R, k2)
    L = format(int(L, 2) ^ int(f_res, 2), '04b')
    
    return permute(L + R, IP_INV)

# --- USER INTERFACE ---
print("--- S-DES Complete Implementation ---")
raw_pt = input("Enter 8-bit Plaintext (e.g., 10101010): ")
raw_key = input("Enter 10-bit Key (e.g., 1010000010): ")

key1, key2 = generate_keys(raw_key)
ciphertext = encrypt(raw_pt, key1, key2)

print(f"\nGenerated Key 1: {key1}")
print(f"Generated Key 2: {key2}")
print(f"Final Ciphertext: {ciphertext}")
