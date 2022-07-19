from caesar_art import caesarcipher_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    
    cipher_text = str()
    hash_map = {}

    if direction == 'decode':
        shift *= -1

    for c in text:
        if c in alphabet:
            if c in hash_map:
                cipher_text+=hash_map[c]
            else:
                if alphabet.index(c)+shift < len(alphabet):
                    hash_map[c]=alphabet[alphabet.index(c)+shift]
                    cipher_text+=hash_map[c]
                else:
                    hash_map[c] = alphabet[alphabet.index(c)+shift - len(alphabet)]
                    cipher_text+=hash_map[c]
        else:
            cipher_text+=c
    return cipher_text
    

def main():
    
    running = 'yes'
    while running == 'yes':
        direction = input("encode or decode? \n").lower()
        text = input("Type you message: \n")
        shift = int(input("Type the shift number: \n"))%26
        print(f"Your {direction}d word is: {caesar(text=text, shift=shift, direction=direction)} \n")

        running = input('Want to keep it running? ')


if __name__ == '__main__':
    print(caesarcipher_logo)
    main()