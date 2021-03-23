#cprint for Python

cprint / colorPrint is a simple prettyprint function for python using ANSI escape characters.
Call cprint(str), inserting the cprint codes surrounded by percent signs(Ex. below).
Using getString(str) directly returns a string instead of printing to stdout.

Several color tags and modifiers can be used in the same tag if they are separated by a comma
###
  Text colors are denoted with the first lower case letter
  -> (r)ed (g)reen (b)lue (c)yan (m)agenta (y)ellow (bl)ack (w)hite
  Background colors are the same, but with a leading "b"

###Modifiers
  (B)old (U)nderlined (I)nverted/reversed (RS)=reset/default

###Macros/Shortcuts
  (warning)   = Yellow, Bold
  (error)     = Red   , Bold, Underlined

###Example code:
```
from cprint import *
cprint("%bc,r%This is pretty high visibility %y%with different colors")
cprint("%bw,b%This text is blue on white, %B,U,I% this is bold, underlined and white on blue")
cprint("%warning%This is a warning!")
cprint("%error%And this is an error")
```
![Screenshot of example code](cprint-screenshot.jpg "Example")
