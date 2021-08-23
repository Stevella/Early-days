# python 3
# madlibs.py reads through a text file and replaces certain keywords
# creates a new file and print the result to the screen
import re,string
#open the oldfile in read mode and newfile in write mode
oldfile = open('madlibs.txt')
newfile = open('New-madlibs.txt','w')
X = ['ADJECTIVE','NOUN','VERB','ADVERB']
#looping through each line in the oldfile
for line in oldfile:
    #use re.findall to create a list of words in each line including punctuations
    wordList = re.findall(r'\w+|[^\s\w]',line)
    #looping through each word in a line
    text = ''
    for word in wordList:
        if word.upper() in X:
            if word[0] in ['A','E','I','O','U']:
                word = input('Enter an %s:\n' %(word))
            else:
                word = input('Enter a %s:\n' %(word))
        punc = string.punctuation
        if word in punc:
            text = text + word
        else:
            text = text + ' ' + word
    text = text.lstrip()
    newfile.write('%s\n' %(text))
newfile.close()
file = open('New-madlibs.txt')
content = file.read()
print(content)
file.close()
oldfile.close()
