# Python Tokenizer
# Carter Crews
# 2017
# For CS475 Sp2017 at UTM.

# Need these to use RegEx to pattern match.
import re
import sys

fileLoc = ""
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
    fileLoc = input("Enter file to parse: ")
    openFile = open(fileLoc)
    return openFile.readlines()

# Main routine that tokenizes the input.
def parseForTokens(openFile):
    global lineFromFile
    global tokens
    
    # Read file line-by-line.
    for line in openFile:
        lineFromFile = line
        while len(lineFromFile) > 0:
            # Remove spaces from input.
            while(lineFromFile[0] == ' '): 
                lineFromFile = lineFromFile[1:]
            token = tokenCheck()
            # If the token is a newline, append the token and a literal newline
            # character.
            if token == '<NL>':
                tokens = tokens + token + '\n'
            # Otherwise just append the token.
            else:
                tokens = tokens + token
# Uses RegExs to tokenize the input.
def tokenCheck():
    tokenString = ""
    global lineFromFile

    # Check every RegEx in the list. Try to match it.
    for token in regexMatch:
        regex = regexMatch[token]
        match = re.match(regex, lineFromFile)
        if match:
            # If matched token is this, check the symbol table location
            # when composing the token.
            if token == 'ID' or token == 'INTEGER' or token == 'REAL':
                # Check if token is already in symbol table. Add if it isn't.
                STLoc = symbolTableCheck(token, match)
                tokenString = '<' + token + ',' + str(STLoc) + '>'
            # If matched token is this, compose the token with the operation.
            elif token == 'EQUAL' or token == 'COMPARISON' or token == 'OP' or token == 'COMBO':
                tokenString = '<' + token + ',' + match.group(0) + '>'
            else:
                tokenString = '<' + token + '>'
            # Remove token that was read from the input.
            lineFromFile = lineFromFile[len(match.group(0)):]
            # If a match is found, return the new token.
            return tokenString

# Search the symbol table to find a token. If it's not found, add it to the
# table.
def symbolTableCheck(token, match):
    global symbolTable

    # Loop through the symbol table.
    for i in range(0, len(symbolTable) // 2):
        # Check if token type matches.
        if token == symbolTable[i*2]:
            # If token type matches, check if the value matches.
            if match.group(0) == symbolTable[i*2+1]:
                return i+1
    # If the token isn't found in the table, add it.
    symbolTable.append(token)
    symbolTable.append(match.group(0))
    # Return the location of the token that was just added.
    return len(symbolTable) // 2

# Print the tokenized code and print the symbol table.
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
