#12/09/25

raw_data = "#Bob# | &30& - %London% | Jane Doe - #Denmark#@Mike@ | $45$ - !New York! |                      ^Sara Lee^ - Canada+Tom+ | ~29~ - Berlin | &Emily Clark& - @France@Anna | #34# - ^Tokyo^ | $Mark Davis$ - %Australia%!George! | 41 - #Rome# | +Kate-Li+ - !Brazil!^Eva M^ | &26& - $Sydney$ | @Chris 44@ - Madrid%Liam% | ~22~ - !Toronto! | #Olivia B# - @Mexico@David | $38$ - %Paris% | ^Nina K^ - #Germany#+Sophia+ | #31# - Amsterdam | &James T& - !Italy!!Emma! | 27 - #Lisbon# | $Henry G$ - %Portugal%"
'''
raw_data = "hello --- world   |||| drew   86"
'''

clean = raw_data.replace("!",",").replace("^",",").replace("£",",").replace("$",",").replace("%",",").replace("&",",").replace("*",",").replace("(",",").replace(")",",").replace("_",",").replace("-",",").replace("+",",").replace("=",",").replace("[",",").replace("]",",").replace("{",",").replace("}",",").replace(";",",").replace(":",",").replace("'",",").replace("@",",").replace("#",",").replace("~",",").replace("/",",").replace("?",",").replace("<",",").replace(">",",").replace(".",",").replace("|",",").replace("  ",",")

space_parts = clean.split(",")

parts = []

for p in space_parts:
    if p.strip() != "":
        parts.append(p.strip())

dataTuple = tuple(parts)


print(dataTuple)