import hashlib
import argparse

def hash_string(input_string: str, algorithm: str = 'sha256') -> str:
    """
    Hash a string using the specified algorithm.

    Args:
        input_string (str): The string to hash.
        algorithm (str): The hashing algorithm to use ('md5', 'sha1', 'sha256', etc.).

    Returns:
        str: The hexadecimal representation of the hash.
    """
    
    hash_object = hashlib.new(algorithm)    
    hash_object.update(input_string.encode('utf-8'))
    
    return hash_object.hexdigest()

def main():
    
    parser = argparse.ArgumentParser(description='Hash a string using a specified algorithm.')
    parser.add_argument('input_string', type=str, help='The string to hash.')
    parser.add_argument('-a', '--algorithm', type=str, default='sha256',
                        choices=['md5', 'sha1', 'sha256', 'sha512'],
                        help='The hashing algorithm to use (default: sha256).')
    
    args = parser.parse_args()
    
    hashed_string = hash_string(args.input_string, args.algorithm)
 
    print(f"Original String: {args.input_string}")
    print(f"{args.algorithm.upper()} Hash: {hashed_string}")

if __name__ == "__main__":
    main()

