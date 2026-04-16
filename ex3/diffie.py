# 1. Get Publicly Shared Values
p = int(input("Enter prime (p): ")) 
g = int(input("Enter base (g): "))  

# 2. Get Private Keys
a_private = int(input("Alice's private key: ")) 
b_private = int(input("Bob's private key: "))  

# 3. Calculate Public Values (to be exchanged)
alice_public = pow(g, a_private, p)
bob_public = pow(g, b_private, p)

print(f"\nAlice sends {alice_public} to Bob")
print(f"Bob sends {bob_public} to Alice")

# 4. Calculate Shared Secret
alice_secret = pow(bob_public, a_private, p)
bob_secret = pow(alice_public, b_private, p)

print(f"\nAlice's Secret: {alice_secret}")
print(f"Bob's Secret: {bob_secret}")
