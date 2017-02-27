# Test code for Python tokenizer.

# Need these to use RegEx to pattern match.
import re
import sys

fileLoc = ""

openFile = readInFile()

# Prompts for file location and opens file.
def readInFile():
    fileLoc = input("Enter file to parse:")
    openFile = open(fileLoc, r)

    return openFile.readlines()


