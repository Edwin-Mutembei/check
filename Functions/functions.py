# question
"""
User Input: ask the user to input a word, and pass that word into a function
that checks if the word starts with an uppercase. If it does output “True”,
otherwise “False”

"""
#  answer

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
