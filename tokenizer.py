# Python Tokenizer

# Need these to use RegEx to pattern match.
import re
import sys

fileLoc = "input.txt"
tokens = ""
symbolTable = []
lineFromFile = ""
regexMatch = {
    "INT" : "int",
    "FLOAT" : "float",
    "REAL" : "\d+\.\d+",
    "INTEGER" : "[\d]+",
    "LSQB" : "\[",
    "RSQB" : "\]",
    "EQUAL" : "=",
    "TAB" : "\t",
    "NL" : "\n",
    "COMPARISON" : "<=|!=|>=|==|<|>]",
    "COMBO" : "\+=|-=|\*=|/=",
    "OP" : "[*/+-]",
    "LPAREN" : "\(",
    "RPAREN" : "\)",
    "LCURL" : "\{",
    "RCURL" : "\}",
    "IF" : "if",
    "ID" : "([\w\d_])+"
}

# Prompts for file location and opens file.
def readInFile():
    #fileLoc = input("Enter file to parse: ")
    openFile = open(fileLoc)
    return openFile.readlines()

def parseForTokens(openFile):
    global lineFromFile
    global tokens
    
    # Read file line-by-line.
    for line in openFile:
        lineFromFile = line
        while len(lineFromFile) > 0:
            while(lineFromFile[0] == ' '):
                lineFromFile = lineFromFile[1:]
            token = tokenCheck()
            if token == '<NL>':
                tokens = tokens + token + '\n'
            else:
                tokens = tokens + token

def tokenCheck():
    tokenString = ""
    global lineFromFile
    
    for token in regexMatch:
        regex = regexMatch[token]
        match = re.match(regex, lineFromFile)
        if match:
            if token == 'ID' or token == 'INTEGER' or token == 'REAL':
                # Check if token is already in symbol table. Add if it isn't.
                STLoc = symbolTableCheck(token, match)
                tokenString = '<' + token + ',' + str(STLoc) + '>'
            elif token == 'EQUAL' or token == 'COMPARISON' or token == 'OP' or token == 'COMBO':
                # Create token with operator.
                tokenString = '<' + token + ',' + match.group(0) + '>'
            else:
                tokenString = '<' + token + '>'
            # Remove token that was read from the input.
            lineFromFile = lineFromFile[len(match.group(0)):]
            # If a match is found, return the new token.
            return tokenString

def symbolTableCheck(token, match):
    global symbolTable
    
    for i in range(0, len(symbolTable) // 2):
        # Check if ID matches.
        if token == symbolTable[i*2]:
            # If ID matches, check if the value matches.
            if match.group(0) == symbolTable[i*2+1]:
                return i+1
    # If the token isn't found in the table, add it.
    symbolTable.append(token)
    symbolTable.append(match.group(0))
    # Return the location of the ID that was just added.
    return len(symbolTable) // 2

def printResults():
    print('*** Tokenized Results ***')
    print(tokens)
    print('*** Symbol Table ***')
    for i in range(0,len(symbolTable) // 2):
        row = str(i+1) + ',' + symbolTable[i*2] + ',' + symbolTable[i*2+1]
        print(row)

# Functions are defined, let's run the tokenizer.
openFile = readInFile()
parseForTokens(openFile)
printResults()
