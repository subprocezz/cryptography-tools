import argparse, base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(plain_text: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt(cipher_text: str, key: bytes) -> str:
    data = base64.b64decode(cipher_text)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plain_text = cipher.decrypt_and_verify(ciphertext, tag)
    return plain_text.decode()

def main():
    parser = argparse.ArgumentParser(description='AES Encryption/Decryption Tool')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the text')
    parser.add_argument('text', type=str, help='Text to encrypt or decrypt')
    parser.add_argument('-k', '--key', type=str, help='Key for encryption or decryption (16, 24, or 32 bytes long)', required=True)

    args = parser.parse_args()

    key = args.key.encode()
    if len(key) not in {16, 24, 32}:
        raise ValueError("Key must be 16, 24, or 32 bytes long")

    if args.encrypt:
        encrypted = encrypt(args.text, key)
        print(f"Encrypted: {encrypted}")
    elif args.decrypt:
        decrypted = decrypt(args.text, key)
        print(f"Decrypted: {decrypted}")
    else:
        print("Please specify either --encrypt or --decrypt.")

if __name__ == "__main__":
    main()

