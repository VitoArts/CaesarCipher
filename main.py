def ceasarCipher(input, key):
    for x in range(len(input)):
        for index in alphabetDict:
            if alphabetDict[index] == input[x]:
                position = index
        newChar = alphabetDict[(position + int(key)) % 26]
        input = input[:x] + newChar + input[x+1:]
    print(input)


if __name__ == '__main__':
    alphabetDict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = 0
    for x in range(26):
        alphabetDict[x+1] = alphabet[x]

    inputStr = input("Enter your string: ")
    inputKey = input("Enter your key (int): ")
    ceasarCipher(inputStr, inputKey)