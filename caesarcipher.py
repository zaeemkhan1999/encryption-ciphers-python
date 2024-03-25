def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

def decrypt(text, k):
    decrypted_text = ""

    # Traverse the text
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - k - 65) % 26 + 65)

        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - k - 97) % 26 + 97)

        # If the character is not a letter, leave it unchanged
        else:
            decrypted_text += char

    return decrypted_text

# Take user inputs
decrypted_text = input("Enter the plain text: ")
key = int(input("Enter the key (shift value): "))

# Decrypt the text
encrypted_text = encrypt(decrypted_text, key)

# Output the decrypted text
print("Encrypted text:", encrypted_text)

# Take user inputs
encrypted_text = input("Enter the encrypted text: ")
shift = int(input("Enter the key (shift value): "))

# Decrypt the text
decrypted_text = decrypt(encrypted_text, shift)

# Output the decrypted text
print("Decrypted text:", decrypted_text)
