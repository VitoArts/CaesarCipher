#Better second version
def ceasarCipherSuperior(inputStr, inputKey):
    newString = ''
    for char in inputStr:
        if char == ' ':
            newString += ' '
        else:
            position = alphabet.find(char)
            newChar = alphabet[(position+inputKey)%26]
            newString += newChar
    print(newString)

#Rough first version
alphabetDict = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
position = 0
spaceKeeper = []

def ceasarCipher(input, key):
    #Ideally we get rid of this double loop in some way
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

if __name__ == '__main__':
    inputStr = input("Enter your string: ")
    inputKey = input("Enter your key (int): ")
    ceasarCipherSuperior(inputStr, int(inputKey))