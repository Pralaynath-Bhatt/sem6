import re
import copy
import sys
import random

def generate_binary_128():
    return bin(random.getrandbits(128))[2:].zfill(128)

# Generate random values
k = generate_binary_128()
m = generate_binary_128()

kbl, kbr = k[:64], k[64:]
mbl, mbr = m[:64], m[64:]

a1, a2 = int(kbl, 2), int(kbr, 2)
a3 = a1 ^ a2

a4 = bin(a3)[2:].zfill(64)
a5, a6 = a4[:32], a4[32:]
a7 = int(a5, 2)

print("128 Bit Key =", k)
print("128 Random Bits Generated =", m)
print("RES/SRES =", bin(a7)[2:].zfill(len(a5)))

# Register lengths
reg_x_length, reg_y_length, reg_z_length = 19, 22, 23

key_one = ""
reg_x, reg_y, reg_z = [], [], []

def loading_registers(key):
    global reg_x, reg_y, reg_z
    reg_x, reg_y, reg_z = [int(bit) for bit in key[:reg_x_length]], [int(bit) for bit in key[reg_x_length:reg_x_length+reg_y_length]], [int(bit) for bit in key[reg_x_length+reg_y_length:]]

def set_key(key):
    global key_one
    if len(key) == 64 and re.match("^([01])+$", key):
        key_one = key
        loading_registers(key)
        return True
    return False

def get_majority(x, y, z):
    return 1 if (x + y + z) > 1 else 0

def get_keystream(length):
    reg_x_temp, reg_y_temp, reg_z_temp = reg_x[:], reg_y[:], reg_z[:]
    keystream = []
    
    for _ in range(length):
        majority = get_majority(reg_x_temp[8], reg_y_temp[10], reg_z_temp[10])
        if reg_x_temp[8] == majority:
            reg_x_temp.insert(0, reg_x_temp[13] ^ reg_x_temp[16] ^ reg_x_temp[17] ^ reg_x_temp[18])
            reg_x_temp.pop()
        if reg_y_temp[10] == majority:
            reg_y_temp.insert(0, reg_y_temp[20] ^ reg_y_temp[21])
            reg_y_temp.pop()
        if reg_z_temp[10] == majority:
            reg_z_temp.insert(0, reg_z_temp[7] ^ reg_z_temp[20] ^ reg_z_temp[21] ^ reg_z_temp[22])
            reg_z_temp.pop()
        keystream.append(reg_x_temp[18] ^ reg_y_temp[21] ^ reg_z_temp[22])
    
    return keystream

def to_binary(plain):
    return ''.join(format(ord(x), '08b') for x in plain)

def convert_binary_to_str(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def encrypt(plain):
    binary = to_binary(plain)
    keystream = get_keystream(len(binary))
    return ''.join(str(int(binary[i]) ^ keystream[i]) for i in range(len(binary)))

def decrypt(cipher):
    keystream = get_keystream(len(cipher))
    binary = ''.join(str(int(cipher[i]) ^ keystream[i]) for i in range(len(cipher)))
    return convert_binary_to_str(binary)

def main_fun():
    key = kbl
    set_key(key)
    print("Using generated key:", key)

    while True:
        choice = input("[0]: Quit\n[1]: Encrypt\n[2]: Decrypt\nPress 0, 1, or 2: ")
        if choice == '0':
            print("Exiting...")
            sys.exit(0)
        elif choice == '1':
            plaintext = input("Enter the plaintext: ")
            encrypted_text = encrypt(plaintext)
            print(f"Ciphertext: {encrypted_text}")
        elif choice == '2':
            while True:
                cipher = input("Enter a ciphertext (binary format): ")
                if re.match("^([01])+$", cipher):
                    decrypted_text = decrypt(cipher)
                    print(f"Decrypted text: {decrypted_text}")
                    break
                else:
                    print("Invalid ciphertext. Must be in binary format.")

if __name__ == "__main__":
    main_fun()
