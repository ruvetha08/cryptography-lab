def simple_cipher_16bit():
    print("--- 16-bit XOR Split Cipher ---")
    
    # 1. Get User Input
    hex_input = input("Enter a 4-character Hex value (e.g., ABCD): ")
    val = int(hex_input, 16)
    
    n1 = (val >> 12) & 0xF
    n2 = (val >> 8) & 0xF
    n3 = (val >> 4) & 0xF
    n4 = val & 0xF
    
    print(f"\n[Step 1] Split 16-bit into Nibbles:")
    print(f"N1: {bin(n1)} | N2: {bin(n2)} | N3: {bin(n3)} | N4: {bin(n4)}")
    
    r1_a = n1 ^ n2
    r1_b = n3 ^ n4
    print(f"\n[Step 2] Round 1 XOR (N1^N2 and N3^N4):")
    print(f"Result A: {hex(r1_a)} | Result B: {hex(r1_b)}")
    
    r2_a = r1_a ^ 0xA  
    r2_b = r1_b ^ 0x5  
    print(f"\n[Step 3] Round 2 XOR with Constants (0xA and 0x5):")
    print(f"Result A: {hex(r2_a)} | Result B: {hex(r2_b)}")
    
    final_output = (r2_a << 12) | (r1_a << 8) | (r2_b << 4) | r1_b
    
    print("\n" + "="*30)
    print(f"Final 16-bit Output (Hex): {hex(final_output).upper()}")
    print(f"Final 16-bit Output (Bin): {bin(final_output)}")
    print("="*30)

if __name__ == "__main__":
    simple_cipher_16bit()
