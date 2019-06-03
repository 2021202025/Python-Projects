import json
import difflib

flag = True

dictionary = json.load(open("data.json"))

def loadDict(word):
    if word in dictionary.keys():
        return(dictionary[word])
    elif(len(difflib.get_close_matches(word, dictionary.keys()))>0):
        closeIn = input("Did you mean %s instead, you dummy? [y/n] " % difflib.get_close_matches(word, dictionary.keys())[0])
        closeIn = closeIn.lower()
        if closeIn == "y":
            return (dictionary[difflib.get_close_matches(word, dictionary.keys())[0]])
        else:
            return "Not found"
    else:
        return "Not a word"

while flag:
    word = input("Word to be searched: ")
    word = word.lower()
    result = loadDict(word)
    print(result)
    search = input("Search more or Exit? ")
    search = search.lower()
    if(search == "exit" or search == "quit"):
        flag = False

