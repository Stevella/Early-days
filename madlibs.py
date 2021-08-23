# python 3
# madlibs.py reads through a text file and replaces certain keywords
# creates a new file and print the result to the screen

#open the oldfile in read mode snd newfile in write mode
oldfile = open('C:\\Users\\Amara\\MyPythonScripts\\madlibs.txt')
newfile = open('C:\\Users\\Amara\\MyPythonScripts\\New-madlibs.txt','w')
X = ['ADJECTIVE','NOUN','VERB','ADVERB']
texts = oldfile.readlines()
#looping through each line in the oldfile
for line in texts:
    wordList = line.split()
    #looping through each word in a line
    for word in wordList:
        if word.upper() in X:
            if word[0] in ['A','E','I','O','U']:
                word = input('Enter an %s:\n' %(word))
            else:
                word = input('Enter a %s:\n' %(word))
        #write in newfile
        newfile.write('%s ' %(word))
    newfile.write('\n')
newfile.close()
file = open('C:\\Users\\Amara\\MyPythonScripts\\New-madlibs.txt')
content = file.read()
print(content)
file.close()
oldfile.close()
