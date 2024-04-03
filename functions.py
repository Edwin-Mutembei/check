word = input('Kindly writte a word: ')
try:
    def upperCaseTest():
        if len(word)>0 and word[0].isupper():
            print('True')
        else: 
            print('False')

    upperCaseTest()

except:
    print("Ensure the word start with an alphabet")
