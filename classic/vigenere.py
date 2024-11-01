import argparse
from string import ascii_lowercase

def vigenere_cipher(plain_text: str, key: str) -> str:
    key = key.lower()
    cipher_text = []
    key_length = len(key)
    
    for i, char in enumerate(plain_text):
        if char in ascii_lowercase:
            shift = ascii_lowercase.index(key[i % key_length])
            new_char = ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]
            cipher_text.append(new_char)
        else:
            cipher_text.append(char)

    return ''.join(cipher_text)

def vigenere_decipher(cipher_text: str, key: str) -> str:
    key = key.lower()
    plain_text = []
    key_length = len(key)
    
    for i, char in enumerate(cipher_text):
        if char in ascii_lowercase:
            shift = ascii_lowercase.index(key[i % key_length])
            new_char = ascii_lowercase[(ascii_lowercase.index(char) - shift) % 26]
            plain_text.append(new_char)
        else:
            plain_text.append(char)

    return ''.join(plain_text)

def brute_force(cipher_text: str, dictionary_path: str) -> None:
    print(f"Trying all keys from dictionary: {dictionary_path}")
    try:
        with open(dictionary_path, 'r') as file:
            for line in file:
                key = line.strip()
                decrypted = vigenere_decipher(cipher_text, key)
                print(f"Key '{key}': {decrypted}")
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main() -> None:
    parser = argparse.ArgumentParser(description='Vigenère Cipher Encryption/Decryption')
    parser.add_argument('text', type=str, help='Text to encrypt or decrypt')
    parser.add_argument('-k', '--key', type=str, help='Key for encryption or decryption', required=False)
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the provided text')
    parser.add_argument('-b', '--brute-force', type=str, help='Path to dictionary file for brute forcing')

    args = parser.parse_args()

    if args.brute_force:
        brute_force(args.text.lower(), args.brute_force)
    elif args.decrypt:
        if not args.key:
            print("Error: A key is required for decryption.")
            return
        decrypted = vigenere_decipher(args.text.lower(), args.key)
        print(f"Decrypted text: {decrypted}")
    else:
        if not args.key:
            print("Error: A key is required for encryption.")
            return
        encrypted = vigenere_cipher(args.text.lower(), args.key)
        print(f"Encrypted text: {encrypted}")

if __name__ == "__main__":
    main()

