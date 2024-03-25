class PermutationCipher:
    def __init__(self, pi):
        self.pi = pi
        self.pi_inv = [0] * len(pi)
        for i in range(len(pi)):
            self.pi_inv[pi[i] - 1] = i + 1

    @staticmethod
    def verify_input(text, pi):
        if not text.isalpha():
            print("Input message must only contain alphabetic characters.")
            return False
        
        if len(text) % len(pi) != 0:
            print("Input message length must be a multiple of", len(pi))
            return False
        
        return True

    def encrypt(self, text):
        cnt = len(text) // len(self.pi)
        substrings = [text[i:i + len(self.pi)] for i in range(0, len(text), len(self.pi))]
        y = ""
        for substr in substrings:
            for j in range(len(substr)):
                y += substr[self.pi[j] - 1]
        return y

    def decrypt(self, text):
        cnt = len(text) // len(self.pi_inv)
        substrings = [text[i:i + len(self.pi_inv)] for i in range(0, len(text), len(self.pi_inv))]
        x = ""
        for substr in substrings:
            for j in range(len(substr)):
                x += substr[self.pi_inv[j] - 1]
        return x

def main():
    # Define the permutation table
    pi = [4, 1, 5, 3, 2]

    # Get input from the user
    message = input("Enter the message to encrypt/decrypt: ").upper()

    # Create an instance of the PermutationCipher class
    pc = PermutationCipher(pi)

    # Verify input validity
    if not pc.verify_input(message, pi):
        return

    # Encrypt the message
    encrypted_message = pc.encrypt(message)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = pc.decrypt(message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
