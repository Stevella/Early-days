#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - delete keyword from the shelve file
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete - delete all keywords from the shelve file

import pyperclip,shelve,sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        x = mcbShelf.pop(sys.argv[2],'key is not in the multi-clipboard')
        #print(x)
elif len(sys.argv) == 2:
    if sys.argv[1].lower()== 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower()== 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
