def julie_encrypt(word):
    square_length = len(word) ** 2
    
    encrypted_word = ""
    
    for char in word:
            new_ascii = ord(char) + square_length
        
            encrypted_word += chr(new_ascii)
    
    return encrypted_word

def julie_decrypt(word):
    square_length = len(word) ** 2
    
    decrypted_word = ""
    
    for char in word:
        new_ascii = ord(char) - square_length
        
        decrypted_word += chr(new_ascii)
    
    return decrypted_word

original_word = input("Enter some string: ")
encrypted_word = julie_encrypt(original_word)
print(original_word)
print(encrypted_word)
decrypted_word = julie_decrypt(encrypted_word)
print(decrypted_word)
