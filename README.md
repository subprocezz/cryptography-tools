# Cryptography Tools

## Overview

This project provides a set of classic cryptographic algorithms implemented in Python, specifically focusing on three ciphers: Caesar Cipher, Vigenère Cipher, and Scytale Cipher. Each algorithm allows for encryption and decryption of text, as well as brute-force attacks to find keys.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Caesar Cipher](#caesar-cipher)
  - [Vigenère Cipher](#vigenère-cipher)
  - [Scytale Cipher](#scytale-cipher)
- [Examples](#examples)
- [License](#license)

## Features

- **Caesar Cipher**: Simple substitution cipher where each letter is shifted by a fixed number.
- **Vigenère Cipher**: Uses a keyword to shift letters based on their position in the keyword.
- **Scytale Cipher**: A transposition cipher that rearranges letters in a specified pattern.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptography-tools.git
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

### Scytale Cipher

To encrypt or decrypt text using the Scytale Cipher:

#### Encrypting Text
```bash
python classic/scytale.py "your_text" -k key_value
```

#### Decrypting Text
```bash
python classic/scytale.py "your_text" -k key_value -d
```

#### Brute Force
```bash
python classic/scytale.py "cipher_text" -b
```

## Examples

Here are a few examples of how to use the ciphers:

- **Caesar Cipher**:
  ```bash
  python classic/caesar.py "hello" -s 3
  ```
  

- **Vigenère Cipher**:
  ```bash
  python classic/vigenere.py "hello" -k key
  ```
  

- **Scytale Cipher**:
  ```bash
  python classic/scytale.py "hello" -k 3
  ```
  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
