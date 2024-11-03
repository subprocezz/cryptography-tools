# Cryptography Tools

## Overview

This project provides a set of classics, modern and hash cryptographic algorithms implemented in Python.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Caesar Cipher](#caesar-cipher)
  - [Vigenère Cipher](#vigenère-cipher)
  - [Nihilist Cipher](#nihilist-cipher)
  - [Hash String](#hash-string)
  - [Hash File](#hash-file)
  - [Crack Hash](#crack-hash)
  - [AES Cipher](#aes-cipher)
- [Examples](#examples)
- [License](#license)

## Features

- **Caesar Cipher**: Simple substitution cipher where each letter is shifted by a fixed number.
- **Vigenère Cipher**: Uses a keyword to shift letters based on their position in the keyword.
- **Nihilist Cipher**: A transposition cipher that rearranges letters in a specified pattern.
- **Hash String**: hashes a string using specified hashing algorithms (like SHA-256 or MD5).
- **Hash File**: calculates and saves the hash of a file using different hashing algorithms (such as SHA-256 or MD5).
- **Crack Hash**: crack hashed passwords using a wordlist. It utilizes the hashlib library to handle different hashing algorithms (like MD5, SHA-1, SHA-256, and SHA-512).
- **AES Cipher**:  It allows users to encrypt or decrypt text using a specified key of 16, 24, or 32 bytes. The encrypt function generates a ciphertext along with a nonce and authentication tag, encoding the result in base64 for easy handling. The decrypt function reverses this process, verifying the integrity of the data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/subprocezz/cryptography-tools.git
   ```
2. Navigate into the project directory:
   ```bash
   cd cryptography-tools
   ```

## Usage

### Caesar Cipher

To encrypt or decrypt text using the Caesar Cipher, use the following commands:

#### Encrypting Text
```bash
python classic/caesar.py "your_text" -s shift_value
```

#### Decrypting Text
```bash
python classic/caesar.py "your_text" -s shift_value -d
```

#### Brute Force
```bash
python classic/caesar.py "cipher_text" -b
```

### Vigenère Cipher

To encrypt or decrypt text using the Vigenère Cipher:

#### Encrypting Text
```bash
python classic/vigenere.py "your_text" -k your_key
```

#### Decrypting Text
```bash
python classic/vigenere.py "your_text" -k your_key -d
```

#### Brute Force
```bash
python classic/vigenere.py "cipher_text" -b path/to/dictionary.txt
```

### Nihilist cipher

To encrypt or decrypt text using the Nihilist cipher:

#### Encrypting Text
```bash
python classic/nihilist.py "your_text" -k key_value
```

#### Decrypting Text
```bash
python classic/nihilist.py "your_text" -k key_value -d
```

### Hash String

To encode text using hash algorithms (md5, sha1, sha256, sha512)

#### Specifyin algorithm
```bash
python hash/hash.py "your_text" -a md5
```

#### Default: sha256
```bash
python hash/hash.py "your_text"
```

### Hash File

To hash file content and save it.

#### Specifyin algorithm and output file
```bash
python hash/hash_file.py path_to_file -a md5 -o output.txt
```

#### Default: (-a: sha256, -o: hash.txt)
```bash
python hash/hash_file.py path_to_file
```

### Crack Hash

To crack hash using a wordlist.

#### Specifyin algorithm
```bash
python hash/crack_hash.py "your_hash" -a md5 -w rockyou.txt
```

#### Default: sha256
```bash
python hash/crack_hash.py "your_hash" -w rockyou.txt
```

### AES Cipher

It allows users to encrypt or decrypt text using a specified key of 16, 24, or 32 bytes.

#### Usage
```bash
python symmetric/AES.py "your_text" -k "your_key"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
