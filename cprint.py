# Felix Albrigtsen 2021

#Usage: cprint("%MARKERS[, ..]% text").
#Example: cprint("%b,U% This is blue and underlined")

#Consider hardcoding \u001b[ in getSequence(), only store the variable part in a dict
#Currently keeping it this way to avoid hardcoding, simplify adapting to other terminals.
escSeq = {
    # Modifiers:
    "B": "\u001b[1m",      #Bold
    "U": "\u001b[4m",      #Underline
    "I": "\u001b[7m",      #Inverted
    "rs": "\u001b[0m",     #Reset
    # FG-Colors:
    "bl": "\u001b[30m",    #Black text
    "r": "\u001b[31m",     #Red text
    "g": "\u001b[32m",     #Green  text
    "y": "\u001b[33m",     #Yellow text
    "b": "\u001b[34m",     #Blue text
    "m": "\u001b[35m",     #Magenta text
    "c": "\u001b[36m",     #Cyan text
    "w": "\u001b[37m",     #White text
    # BG-Colors
    "bbl": "\u001b[40m",   #Black background
    "br": "\u001b[41m",    #Red background
    "bg": "\u001b[42m",    #Green background
    "by": "\u001b[43m",    #Yellow background
    "bb": "\u001b[44m",    #Blue background
    "bm": "\u001b[45m",    #Magenta background
    "bc": "\u001b[46m",    #Cyan background
    "bw": "\u001b[47m"    #White background
}
macros = {
    "warning": ["y", "B"],
    "error": ["r", "B", "U"]
}

#Translate prettyprint codes to ANSI codes
def getSequence(codeStr):
    codes = codeStr.split(",") #Split lists of several codes

    for code in codes:  #Substitute macro shortcuts into the list
        if code in macros:
            codes.remove(code)
            codes += macros[code]

    outSeq = ""
    for code in codes:
        if code in escSeq:
            outSeq += escSeq[code] #Simple dictionary lookup, insert the ANSI code corresponding to our symbol
        else:
            print(code)
            raise ValueError("Invalid prettyprint code") #Raise exception on invalid codes.
        
    return outSeq

    
def getString(inStr):
    pos = 0
    out = "" # String that stores the result after "translation"

    while pos < len(inStr):
        if (inStr[pos] == "%") and (pos>0 or inStr[pos-1] != "\\"): # Found a non-escaped %
            code = ""
            pos += 1
            while inStr[pos] != "%": # Scan until the closing %
                code += inStr[pos]
                pos += 1
            pos += 1
            out += getSequence(code) # Look up the escape character and insert it
        if pos < len(inStr): 
            out += inStr[pos]       # Normal(non-%) characters, send to output
        pos += 1
    return out

def cprint(inStr):
    print(getString(inStr) + getSequence("rs"))

# EXAMPLES / TESTS
# cprint("%bc,r%This is pretty high visibility %y%with different colors")
# cprint("%bw,b%This text is blue on white, %B,U,I% this is bold, underlined and white on blue")
# cprint("%warning%This is a warning!")
# cprint("%error%And this is an error")
