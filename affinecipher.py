# Extended Euclidean Algorithm for finding modular inverse
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# Affine cipher encryption function
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])

# Affine cipher decryption function
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])

# Main function
def main():
    # Prompt user to enter text and key
    text = input("Enter the plaintext (only uppercase letters): ")
    a = int(input("Enter the key 'a' (an integer coprime to 26): "))
    b = int(input("Enter the key 'b' (an integer from 0 to 25): "))

    # Validate key 'a' to be coprime with 26
    while True:
        gcd, _, _ = egcd(a, 26)
        if gcd == 1:
            break
        else:
            print("Key 'a' must be coprime with 26. Please enter a valid key.")
            a = int(input("Enter the key 'a' (an integer coprime to 26): "))

    key = [a, b]

    # Encrypt the text
    affine_encrypted_text = affine_encrypt(text, key)
    print('Encrypted Text: {}'.format(affine_encrypted_text))

    # Decrypt the text
    decrypted_text = affine_decrypt(affine_encrypted_text, key)
    print('Decrypted Text: {}'.format(decrypted_text))

if __name__ == '__main__':
    main()
