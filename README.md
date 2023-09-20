# Crypto Quadratic Defender (CQD)
A completely new Cryptography technique created exclusively for JSON Understandable Language Intelligence Engine. (J.U.L.I.E)
This Python script provides simple encryption and decryption functions based on the square length of the input word.

## Usage

To use this script, follow these steps:

1. Clone the repository.
2. Run the script.
3. Enter a string for encryption.
4. The encrypted and decrypted strings will be displayed.

## Example

```python
Enter some string: I'm not in danger..I' the Danger

Encrypted: щЧѭРѮѯѴРѩѮРѤѡѮѧѥѲЮЮщЧРѴѨѥРфѡѮѧѥѲ
Decrypted: I'm not in danger..I' the Danger
```
## Encryption

def julie_encrypt(word):: This line defines a Python function named julie_encrypt that takes one argument, word. This function will be used to encrypt a given word.

square_length = len(word) ** 2: Here, you calculate the square of the length of the input word and store it in the square_length variable. This value is used as an encryption key.

encrypted_word = "": Initialize an empty string called encrypted_word where you will build the encrypted result.

for char in word:: Start a loop to iterate through each character in the input word.

new_ascii = ord(char) + square_length: Calculate a new ASCII value for each character in the input word by adding the square_length to the ASCII value of the character. This is the encryption process.

encrypted_word += chr(new_ascii): Append the character with the new ASCII value to the encrypted_word string.

return encrypted_word: After processing all characters in the input word, return the fully encrypted word.

## Decryption

def julie_decrypt(word):: This line defines another Python function named julie_decrypt that takes one argument, word. This function will be used to decrypt an encrypted word.

square_length = len(word) ** 2: Similar to the encryption function, you calculate the square of the length of the input word and store it in square_length. This value serves as the decryption key.

decrypted_word = "": Initialize an empty string called decrypted_word where you will construct the decrypted result.

for char in word:: Start a loop to iterate through each character in the input word.

new_ascii = ord(char) - square_length: Calculate a new ASCII value for each character by subtracting the square_length from the ASCII value of the character. This is the decryption process, which reverses the encryption.

decrypted_word += chr(new_ascii): Append the character with the new ASCII value to the decrypted_word string.

return decrypted_word: After processing all characters in the input word, return the fully decrypted word.
