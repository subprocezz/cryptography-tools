from string import ascii_lowercase
import argparse

def caesar_cipher(plain_text: str, shift: int) -> str:
    alphabet: str = ascii_lowercase
    length: int = len(alphabet)
    cipher_text: str = ""

    for char in plain_text:
        if char in alphabet:
            index: int = (alphabet.index(char) + shift) % length
            cipher_text += alphabet[index]
        else:
            cipher_text += char

    return cipher_text

def caesar_decipher(cipher_text: str, shift: int) -> str:
    return caesar_cipher(cipher_text, -shift)

def brute_force(cipher_text: str) -> None:
    print("Trying all possible shifts:")
    for shift in range(1, 26):
        decrypted: str = caesar_decipher(cipher_text, shift)
        print(f"#{shift}: {decrypted}")

def main() -> None:
    parser = argparse.ArgumentParser(description='Cesar Cipher Encryption/Decryption')
    parser.add_argument('text', type=str, help='Text to encrypt or decrypt')
    parser.add_argument('-s', '--shift', type=int, help='Shift value (1-25)', required=False)
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the provided text')
    parser.add_argument('-b', '--brute-force', action='store_true', help='Attempt to brute force the provided text')


    args = parser.parse_args()

    if args.brute_force:
        brute_force(args.text.lower())
    elif args.decrypt:
        decrypted = caesar_decipher(args.text.lower(), args.shift)
        print(f"Decrypted text: {decrypted}")
    else:
        encrypted = caesar_cipher(args.text.lower(), args.shift)
        print(f"Encrypted text: {encrypted}")

if __name__ == "__main__":
    main()

