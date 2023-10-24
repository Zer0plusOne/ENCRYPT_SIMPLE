# Encriptacion de un texto por una llave
import sys
import os

logo = '''\033[33m                                                                                                                                                                                                                                                                  
                      ██████████                                                            
                  ████░░░░░░░░░░██████                                                    
                ██░░░░░░░░░░░░░░░░░░░░██                                                    
              ██░░░░░░░░░░░░░░░░░░░░░░░░██    ████                                          
            ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██                                          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░████████████████████████████████            
          ██░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
          ██░░░░██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
          ██░░░░██      ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██          
          ██░░░░██      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░░░░░▓▓░░░░░░░░██            
          ██░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░██████░░██  ██░░░░██  ████████              
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██    ██      ████                          
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░██  ██░░██                                          
              ██░░░░░░░░░░░░░░░░░░░░░░░░██    ████                                          
                ██░░░░░░░░░░░░░░░░░░░░██                                                    
                  ████░░░░░░░░░░██████                                                      
                  ░░░░▓▓▓▓▓▓▓▓▓▓░░░░░░\033[97m

                                    LOCKER by Zer0                 
                        Github: https://github.com/Zer0plusOne/
\033[97m
'''
# Menu de eleccion
def menu():
    os.system("cls")
    print(logo)
    print("Menu:")
    print("1. Encryption")
    print("2. Decryption")
    choice = input("SELECT: ")

    if choice == "1":
        text = input("Enter the text to encrypt: ")
        key = int(input("Enter the key: "))
        encrypted_text = encrypt(text, key)
        print("Encrypted Text:", encrypted_text)
        menu()
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        key = int(input("Enter the key: "))
        decrypted_text = decrypt(text, key)
        print("Decrypted Text:", decrypted_text)
        menu()
    else:
        print("Invalid choice. Please try again.")
        menu()

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + key)
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        decrypted_char = chr(ord(char) - key)
        decrypted_text += decrypted_char
    return decrypted_text

menu()