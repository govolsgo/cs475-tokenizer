# Test code for Python tokenizer.

# Need these to use RegEx to pattern match.
import re
import sys

fileLoc = ""
tokens = []
symbolTable = []
lineFromFile = ""

openFile = readInFile()

regexMatch = {
    "ID" : "([\w\d_])+",
    "INT" : "int",
    "FLOAT" : "float",
    "INTEGER" : "[\d]+",
    "REAL" : "\d+\.\d+",
    "LSQB" : "\[",
    "RSQB" : "\]",
    "EQUAL" : "=",
    "TAB" : "\t",
    "NL" : "\n",
    "COMPARISON" : "(< | = | > | (<=) | (!=) |(>=) |(==) | (===) | (!==))",
    "OP" : "[*/+-]",
    "LPAREN" : "\(",
    "RPAREN" : "\)",
    "LCURL" : "\{",
    "RCURL" : "\}",
    "IF" : "if"  
}

# Prompts for file location and opens file.
def readInFile():
    fileLoc = input("Enter file to parse:")
    openFile = open(fileLoc, r)

    return openFile.readlines()

def parseForTokens(openFile):
    for line in openFile:
        lineFromFile = line
        while len(lineFromFile) > 0:
            while(lineFromFile[0] == ' '):
                lineFromFile = lineFromFile[1:]
            token = tokenCheck()
                    

def tokenCheck():
    for token in regexMatch:
        regex = regexMatch[token]
        matches = re.match(regex, lineFromFile)
        if matches:
            if (token == "ID" || token == "INTEGER" || token == "REAL"):
                
