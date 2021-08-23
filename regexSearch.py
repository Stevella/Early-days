# python 3
#regexSearch.py opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. results are printed to the screen
import os,re,glob,sys
#print(sys.argv[1])
if len(sys.argv) < 3:
    #ask for directory and regexpattern if commandline arguments is insufficient
    folder = input('Enter the folder path: ')
    regexPattern = input('Enter the Regex: ')
else:
    folder = sys.argv[1]
    regexPattern = sys.argv[2]
# verify the provided folder path is a directory
if os.path.isdir(r'%s' %(folder)):
    #using os.walk to find the files recursively(folders,subfolders)
    # r= root, d = directories, f = files
    for r,d,f in os.walk(folder):
        for file in f:
            if '.txt' in file:
                fhand = open(os.path.join(r, file))
                for line in fhand:
                    match = re.findall(r'%s' %(regexPattern),line)
                    if len(match) > 0:
                        print('the file [%s] has %s match(es).' %(file,len(match)))
                        print(match)
