import hashlib
import argparse

def crack_hash(target_hash: str, wordlist_file: str, algorithm: str) -> str:
    """
    Attempt to crack the given hash using a wordlist.

    Args:
        target_hash (str): The hash to crack.
        wordlist_file (str): Path to the wordlist file.
        algorithm (str): The hashing algorithm to use.

    Returns:
        str: The cracked password, or 'Not found' if unsuccessful.
    """
    hash_function = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }

    if algorithm not in hash_function:
        raise ValueError(f"Unsupported algorithm: {algorithm}. Choose from {list(hash_function.keys())}.")
    with open(wordlist_file, 'r', encoding='utf-8') as f:
        for line in f:
            candidate = line.strip()
            if hash_function[algorithm](candidate.encode()).hexdigest() == target_hash:
                return candidate  

    return 'Not found'  

def main() -> None:
    parser = argparse.ArgumentParser(description='Crack a hash using a wordlist.')
    parser.add_argument('hash', type=str, help='The hash to crack.')
    parser.add_argument('wordlist', type=str, help='Path to the wordlist file.')
    parser.add_argument('-a', '--algorithm', type=str, default='md5',
                        choices=['md5', 'sha1', 'sha256', 'sha512'],
                        help='Hash algorithm to use (default: md5).')

    args = parser.parse_args()

    cracked_password = crack_hash(args.hash, args.wordlist, args.algorithm)
    print(f"Cracked Password: {cracked_password}")

if __name__ == "__main__":
    main()

