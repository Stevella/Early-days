# python 3
#regexSearch.py opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. results are printed to the screen
import os,re,glob,sys
#print(sys.argv)
if len(sys.argv) < 3:
    #ask for directory and regexpattern if commandline arguments is insufficient
    folder = input('Enter the folder path: ')
    regexPattern = input('Enter the Regex: ')
else:
    folder = sys.argv[1]
    regexPattern = sys.argv[2]
# verify the provided folder path is a directory
if os.path.isdir(r'%s' %(folder)):
    #use os.listdir to find the files but not recursive
    #fileNames = os.listdir(r'%s' %(folder))
    #using glob.glob to find the files recursively(folders,subfolders)
    filePath = [file for file in glob.glob(r'%s\**\*.txt' %(folder), recursive = True)]
    #print(filePath)
    for file in filePath:
        fhand = open(file)
        for line in fhand:
            match = re.findall(r'%s' %(regexPattern),line)
            if len(match) > 0:
                print('the file [%s] has %s match(es).' %(os.path.basename(file),len(match)))
                print(match)
