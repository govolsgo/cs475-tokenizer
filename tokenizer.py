# Python tokenizer.

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
    "COMPARISON" : "(< | = | > | <= | != | >= | == )",
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
    # Read file line-by-line.
    for line in openFile:
        lineFromFile = line
        while len(lineFromFile) > 0:
            while(lineFromFile[0] == ' '):
                lineFromFile = lineFromFile[1:]
            token = tokenCheck()
                    

def tokenCheck():
    tokenString = ""
    
    for token in regexMatch:
        regex = regexMatch[token]
        match = re.match(regex, lineFromFile)
        if match:
            if token == "ID" or token == "INTEGER" or token == "REAL":
                # Check if token is already in symbol table. Add if it isn't.
                STLoc = symbolTableCheck(### Args ###
                )
                tokenString = '<' + token ',' + STLoc + '>'
            elif token == "EQUAL" or token == "COMPARISON" or token == "OP":
                # Create token with operator.
                tokenString = '<' + token + ',' + match.group(0) + '>'
            else:
                tokenString = '<' + token + '>'
            # Remove token that was read from the input.
            lineFromFile = lineFromFile[len(match.group(0)):]
            # If a match is found, return the new token.
            return tokenString

def symbolTableCheck(### Args ###
):
    
