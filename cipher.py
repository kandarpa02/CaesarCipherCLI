import argparse
import string

def caesar_cipher(message, key, mode="encrypt"):
    
    if mode == "decrypt":
        shift = 26 - (key % 26)
    else:  # Default to "encrypt"
        shift = key % 26

    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )

    return message.lower().translate(cipher)

def main():
    parser = argparse.ArgumentParser(description = 'A CLI tool for Caesar Cipher encryption and decryption')
    parser.add_argument('message', help = 'The text to be processed')
    parser.add_argument("key", type=int, help="The number of shifts (positive integer)")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose 'encrypt' or 'decrypt'")



    args = parser.parse_args()
        
    result = caesar_cipher(args.message, args.key, args.mode)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()





