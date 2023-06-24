import string
#Lorenzo Murillo IV 
#CECS 378 Spring 23

#function that will decrypt
#NOTE: The key that is being passed should be in the order that the encrpytion one used
def decryption(phrase, key):
    #string that holds the alphabet
    alphaSet = string.ascii_lowercase
    #create an empty key map to have alphabet mapped to key 
    keyMap = {}
    #map all values in alphabet to key, this can probably be done a lot cleaner (come back to this and figure out better solution)
    for index in range(len(key)):
        #keyMap will have alphabet : keyLetter
        keyMap[alphaSet[index]] = key[index]
    
    #create empty string to store scrubbed phrase
    cleanPhrase = ''
    print(keyMap)
    #iterate through phrase
    for letter in phrase:
        #determine if character is in english alphabet
        if(letter.isalpha()):
            #concatenate string with each alpha letter
            cleanPhrase += letter.lower()

    #create an empty string that will hold the decryption result
    decryptionPhrase = ''
    #iterate through cleanphrase by character
    for character in cleanPhrase:
        #determine if character is in map
        if(character in keyMap):
            #add the mapped value to string
            decryptionPhrase += keyMap.get(character)

    #print encrypted message
    print("Decrypted Message:  " + decryptionPhrase)

def main():
    #ask user for phrase
    phrase = input("Enter the phrase you would like decyrpted: ")
    #make the phrase all lowercase 
    phrase = phrase.lower()

    #ask user for key
    key = input("Enter a key for your decryption substitution (english alphabet, a-z): ")
    #if the string entered is not 26 ask again 
    while(len(key) != 26):
        key = input("invalid key size, please enter the english alphabet: ")
    #have the key be all lowercase
    key = key.lower()

    #call to encrpytion function 
    decryption(phrase, key)

if __name__  == '__main__':
    main()
