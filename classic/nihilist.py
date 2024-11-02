import argparse
from typing import Optional

def create_square() -> list[list[str]]:
    alphabet: str = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    return [list(alphabet[i:i + 5]) for i in range(0, 25, 5)]

def find_position(char: str, square: list[list[str]]) -> Optional[tuple[int, int]] :
    for row in range(5):
        for col in range(5):
            if square[row][col] == char:
                return row, col
    return None

def encrypt(plain_text: str, key: str) -> str:
    square: list[list[str]] = create_square()
    key_numbers: str = ''.join([str((ord(k) - ord('A')) // 5 + 1) for k in key])
    plain_text: str = plain_text.replace(" ", "").upper()

    encrypted_numbers: list[str] = []
    for char in plain_text:
        if char == 'J':
            char = 'I'  
        position: Optional[tuple[int, int]] = find_position(char, square)
        if position:
            row, col = position
            encrypted_numbers.append(str(row + 1))
            encrypted_numbers.append(str(col + 1))
    
    return key_numbers + ''.join(encrypted_numbers)

def decrypt(cipher_text: str, key: str) -> str: 
    square: list[list[str]] = create_square()
    key_length: int = len(key)
    key_numbers: str = ''.join([str((ord(k) - ord('A')) // 5 + 1) for k in key])
    
    cipher_numbers: str = cipher_text[len(key_numbers):]
    
    plain_text: list[str] = []
    for i in range(0, len(cipher_numbers), 2):
        row: int = int(cipher_numbers[i]) - 1
        col: int = int(cipher_numbers[i + 1]) - 1
        plain_text.append(square[row][col])

    return ''.join(plain_text)

def main():
    parser = argparse.ArgumentParser(description='Nihilist Cipher Encryption/Decryption')
    parser.add_argument('text', type=str, help='Text to encrypt or decrypt')
    parser.add_argument('-k', '--key', type=str, required=True, help='Key for encryption or decryption')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the provided text')

    args = parser.parse_args()

    if args.decrypt:
        decrypted = decrypt(args.text.upper(), args.key)
        print(f"Decrypted text: {decrypted}")
    else:
        encrypted = encrypt(args.text.upper(), args.key)
        print(f"Encrypted text: {encrypted}")

if __name__ == "__main__":
    main()

