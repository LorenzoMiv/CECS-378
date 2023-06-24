import string
#Lorenzo Murillo IV 
#CECS 378 Spring 23

#function that will encrypt
def encryption(phrase, key):
    #string that holds the alphabet
    alphaSet = string.ascii_lowercase
    #create an empty key map to have alphabet mapped to key 
    keyMap = {}
    #map all values in alphabet to key, this can probably be done a lot cleaner (come back to this and figure out better solution)
    for index in range(len(key)):
        keyMap[key[index]] = alphaSet[index]

    #create empty string to store scrubbed phrase
    cleanPhrase = ''

    #iterate through phrase
    for letter in phrase:
        #determine if character is in english alphabet
        if(letter.isalpha()):
            #concatenate string with each alpha letter
            cleanPhrase += letter.lower()

    ###test###
    #print(cleanPhrase)

    #create an empty string that will hold the encryption result
    encryptionPhrase = ''
    #iterate through cleanphrase by character
    for character in cleanPhrase:
        #determine if character is in map
        if(character in keyMap):
            #add the mapped value to string
            encryptionPhrase += keyMap.get(character)

    #print encrypted message
    print("Encrypted Message:  " + encryptionPhrase)


def main():
    #ask user for phrase
    phrase = input("Enter the phrase you would like encyrpted: ")
    #make the phrase all lowercase 
    phrase = phrase.lower()

    #ask user for key
    key = input("Enter a key for your encryption substitution (english alphabet, 26 letters): ")
    #if the string entered is not 26 ask again 
    #NOTE: this does not account for repeated values, that edge case was not in the write up
    #      so I am assuming that the user is competent enough to enter 26 characters that belong to 
    #      the english alphabet.
    while(len(key) != 26):
        key = input("invalid key size, please enter the english alphabet: ")
    #have the key be all lowercase
    key = key.lower()

    #call to encrpytion function 
    encryption(phrase, key)

if __name__  == '__main__':
    main()
