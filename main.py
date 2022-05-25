alphabet = "abcdefghijklmnopqrstuvwxyz"
position = 0

#Application to print all 25 possibilities to find out if the cipher used in a caesarcipher.
def caesar_cipher_cracker(input_str):
    print("All keys: ")
    for count in range(25):
        print("if key = " + str(count+1))
        caesar_cipher(input_str, count+1)

def caesar_cipher(input_str, input_key):
    new_string = ''
    for char in input_str:
        if char == ' ':
            new_string += ' '
        else:
            position = alphabet.find(char)
            new_char = alphabet[(position+input_key)%26]
            new_string += new_char
    print(new_string)

if __name__ == '__main__':
    input_str = input("Enter your string: ")
    input_key = input("Enter your key (int): ")
    caesar_cipher(input_str, int(input_key))
    caesar_cipher_cracker(input_str)