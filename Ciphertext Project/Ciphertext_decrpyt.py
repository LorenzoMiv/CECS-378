import itertools
import string
import random
#Lorenzo Murillo IV
#CECS 378 Lab Assignment 1
#Due: 2/24/2022


#a function that creates takes in a randomized key and swaps elements
#params: cipherText, key
#        cipherText is the original text that is give and key is a possible key
#return: a key for mapping to the alphabet 
#we iterate over the provided key and swap elements 
#once a better score is deteremined we save that score
#when keyScore is returned with the best we return the key
def hillClimb(cipherText, key):
    keyScore = 0
    for i in range(len(key) - 1):
        for j in range(i + 1, len(key)):
            temp = list(key)
            temp[i], temp[j] = temp[j], temp[i]
            testText = keyTextTranslator(cipherText, temp)
            testKey = isEnglish(testText)
            if(testKey > keyScore):
                print("Running... Key Score: ", keyScore)
                keyScore = testKey
                key = list(temp)
    return key

#a functin that returns the phrase of a ciphertext with a key
#params: ciphertext, key
#        original cipherText is provided and the key from hillclimb func
#return: decrypted phrase
#this function will translate the given cipher text with known key 
#iterate through cipherText and replace with correct sub
#       example: someKey = hillClimb('CipHer', 'abc..')
#                print(keyTextTranslator('CipHer', someKey))
def keyTextTranslator(cipherText, key):
    keyMap = mapAlphabet(key)
    decryptionPhrase = ''

    for character in cipherText:
        if(character in keyMap):
            decryptionPhrase += keyMap.get(character)
    return decryptionPhrase

#a function that reads in the file
#params: none
#return: a set of words
#iterate through a provided file and store into a set
#return the set
def wordLoader():
    with open('words_alpha.txt') as wordFile:
        words = set(wordFile.read().split())
    return words

#define a variable to reference valid words in a set
englishWords = wordLoader()

#a function that determines if the given text is english 
#params: text - takes in some text to determine if a phrase is english
#return: a score that decides how close the phrase is to english
#iterate through the given text provdided
#iterate through the external dictionary 
#score on how close to an english word we have
def isEnglish(text):
    score = 0
    for i in range(len(text)):
        for word in englishWords:
            if text[i:].startswith(word):
                score += len(word)
                break
    return score/len(text)

#a function that takes in the discovered key and maps it to the alphabet
#params: key - a known key
#return: keyMap - used for translating a cipherText
#use an alphabet list to map the key : alphabet
def mapAlphabet(key):
    alphabet = []
    for letter in string.ascii_lowercase:
        alphabet.append(letter)

    keyMap = {}
    for i in range(len(alphabet)):
        keyMap[alphabet[i]] = key[i]

    return keyMap

#main function 
def main():
    #alphabet that will be used to generate a random key
    alphabet = []

    for letter in string.ascii_lowercase:
        alphabet.append(letter)
    #to track score
    maxScore = 0
    #to track best key
    bestKey = list(alphabet)
    random.shuffle(alphabet)
    #ask for ciphertext
    result = input("Please enter a cipherText you would like decrypted: ")
    for i in range(1000):
        tempScore = hillClimb(result, alphabet)
        if(tempScore > maxScore):
            maxScore = tempScore
            bestKey = list(alphabet)
        else:
            break

    knownKey = mapAlphabet(bestKey)        
    phraseDecryption = keyTextTranslator(result, knownKey)
    print(phraseDecryption)
#a main function that implements the program
if __name__ == '__main__':
    main()
