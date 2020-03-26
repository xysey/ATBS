#! python3
"""
mcb.pyw - Saves and loads pieces of text to the clipboard.
Usage:  py.exe mcb.pyw save <keyword> - Saves a clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to the clipboard.
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")
# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    # delete the keyword and the content
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    # delete all the data in the shelve
    elif sys.argv[1].lower() == "delete":
        keys = list(mcbShelf.keys())
        for i in range(len(mcbShelf)):
            del mcbShelf[keys[i]]
    # copy the content of the keyword to the clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
