import argparse

def scytale_cipher(plain_text: str, key: int) -> str:
    # Remove spaces and convert to lowercase
    plain_text = plain_text.replace(" ", "").lower()
    length = len(plain_text)

    # Create a list for the cipher text
    cipher_text = [''] * key

    # Fill the rows
    for i in range(length):
        cipher_text[i % key] += plain_text[i]

    # Join the rows to form the cipher text
    return ''.join(cipher_text)

def scytale_decipher(cipher_text: str, key: int) -> str:
    length = len(cipher_text)
    rows = (length + key - 1) // key  # Calculate number of rows needed

    # Create a list for the plain text
    plain_text = [''] * rows

    # Fill the columns
    for i in range(length):
        plain_text[i // key] += cipher_text[i]

    # Join the rows to form the plain text
    return ''.join(plain_text).strip()

def brute_force(cipher_text: str) -> None:
    print("Trying all possible keys:")
    for key in range(2, len(cipher_text) + 1):
        decrypted = scytale_decipher(cipher_text, key)
        print(f"Key {key}: {decrypted}")

def main() -> None:
    parser = argparse.ArgumentParser(description='Scytale Cipher Encryption/Decryption')
    parser.add_argument('text', type=str, help='Text to encrypt or decrypt')
    parser.add_argument('-k', '--key', type=int, help='Key for encryption or decryption', required=False)
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the provided text')
    parser.add_argument('-b', '--brute-force', action='store_true', help='Attempt to brute force the provided text')

    args = parser.parse_args()

    if args.brute_force:
        brute_force(args.text.replace(" ", "").lower())
    elif args.decrypt:
        if args.key is None:
            print("Error: A key is required for decryption.")
            return
        decrypted = scytale_decipher(args.text.replace(" ", "").lower(), args.key)
        print(f"Decrypted text: {decrypted}")
    else:
        if args.key is None:
            print("Error: A key is required for encryption.")
            return
        encrypted = scytale_cipher(args.text.replace(" ", ""), args.key)
        print(f"Encrypted text: {encrypted}")

if __name__ == "__main__":
    main()

