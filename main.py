
alphabetDict = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
position = 0
spaceKeeper = []

def ceasarCipher(input, key):
    for x in range(len(input)):
        for index in alphabetDict:
            if alphabetDict[index] == input[x]:
                position = index
        newChar = alphabetDict[(position + int(key)) % 26]
        input = input[:x] + newChar + input[x+1:]
    if spaceKeeper != []:
        for space in range(len(spaceKeeper)):
            input = input[:spaceKeeper[space]] + ' ' + input[spaceKeeper[space]+1:]
    print(input)

def findSpace(input):
    for index in range(len(input)):
        if input[index] == ' ':
            spaceKeeper.append(index)

if __name__ == '__main__':
    for x in range(26):
        alphabetDict[x+1] = alphabet[x]
    inputStr = input("Enter your string: ")
    if inputStr.count('') > 0:
        findSpace(inputStr)
    inputKey = input("Enter your key (int): ")
    ceasarCipher(inputStr, inputKey)