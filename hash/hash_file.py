import hashlib
import argparse

def hash_file(file_path: str, algorithm: str = 'sha256') -> str:
    """
    Hash the contents of a file using the specified algorithm.

    Args:
        file_path (str): The path to the file to hash.
        algorithm (str): The hashing algorithm to use ('md5', 'sha1', 'sha256', etc.).

    Returns:
        str: The hexadecimal representation of the hash.
    """
    
    hash_object = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_object.update(chunk)
    
    return hash_object.hexdigest()

def save_file(file_path: str, hash_string: str) -> None:
    with open(file_path, 'w') as file:
        file.write(hash_string)
    
def main() -> None:
    parser = argparse.ArgumentParser(description='Hash the contents of a file using a specified algorithm.')
    parser.add_argument('file_path', type=str, help='The path to the file to hash.')
    parser.add_argument('-a', '--algorithm', type=str, default='sha256',
                        choices=['md5', 'sha1', 'sha256', 'sha512'],
                        help='The hashing algorithm to use (default: sha256).')
    parser.add_argument('-o', '--output', type=str, default='hash.txt',help='The path to the file to save hash', required=False)

    args = parser.parse_args()    
    hashed_string: str = hash_file(args.file_path, args.algorithm)
    
    print(f"File: {args.file_path}")
    print(f"{args.algorithm.upper()} Hash: {hashed_string}")

    save_file(args.output, hashed_string)
    print(f"Hash saved to {args.output}")

if __name__ == "__main__":
    main()

