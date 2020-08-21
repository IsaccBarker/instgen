#!/usr/bin/python

import os.path
import sys

template = """
[Desktop Entry]
Type=$(TYPE)
Encoding=UTF-8
Name=$(NAME)
Comment=$(DESC)
Icon=$(ICON)
Exec=$(EXEC)
Terminal=$(TERM)
Categories=$(TAGS)
"""

glosary = """A  \t:\tApplication
L   \t:\tLink
D   \t:\tDirectory
Y/n \t:\tYes / No
none\t:\tNo icon
.   \t:\tEnd List
"""

def usage():
    print("""instgen -- a simple utility in python for generating a .desktop file for an application for free desktop based systems.
    GLOSARY:
        {}
    USAGE:
        instgen stdin                                                                                                                        ~ Will take arguments from stdin
        instgen Type[A/l/d] Name PathToExecutable PathToIcon Terminal[Y/n] Description Owner(all for all) Tags(; separated string in quotes) ~ Takes arguments from command line
    AUTHOR
        Milo Banks (Copyright 2020 under GNU GPL)
    """.format(glosary.replace("\n", "\n\t")))

filepath = ""
typ, nme, exe, ico, trm, des, usr = "", "", "", "", "", "", ""
tags = []

if (len(sys.argv) == 1):
    print("Type stdin for stdin mode!", file=sys.stderr)
    usage()
    exit(1)
elif (sys.argv[2] == "stdin"):
    # Get from stdin
    typ = input("Type [A/l/d]:        ")
    nme = input("Name of application: ")
    exe = input("Path to executable:  ")
    ico = input("Path to icon:        ")
    trm = input("Terminal [Y/n]:      ")
    des = input("Description:         ")
    usr = input("Owner (all for all): ")

    while (True):
        tag = input(" Tags (end with .):  ")
        if (tag == "."):
            break

        tags.append(tag)
else:
    # Get from command line
    if (len(sys.argv) != 9):
        print("Insuficant arguments!", file=sys.stderr)
        usage()
        exit(1)

    typ = sys.argv[1]
    nme = sys.argv[2]
    exe = sys.argv[3]
    ico = sys.argv[4]
    trm = sys.argv[5]
    des = sys.argv[6]
    usr = sys.argv[7]
    tags = sys.argv[8].split(";")

print("-> Parsing input....")
# If we don't want an icon, we need to set it to a valid filename.
if (ico.upper() == "NONE"):
    ico = exe

exe = os.path.abspath(exe)
ico = os.path.abspath(ico)

if (usr == "all"):
    filepath = "/usr/share/applications"
else:
    filepath = "/home/" + usr + "/.local/share/applications"

if (typ.upper() in "A"):
    typ = "Application"
elif (typ.upper() in "L"):
    typ = "Link"
elif (typ.upper() in "D"):
    typ = "Directory"
else:
    print("Type `" + typ + "` does not exist. See above.", file=sys.stderr)
    exit(1)

if (trm.upper() in "Y" or trm == ""):
    trm = "true"
else:
    trm = "false"

print("-> Validating environment....")

# Does filepath exist?
print(" -> Does appropriate .desktop directory exist?")
if (not os.path.isdir(filepath)): 
    if (usr == "all"):
        print(filepath + " does not exist.", file=sys.stderr)
    else:
        print(filepath + " does not exist. Does the user `" + usr+ "` exist?")

    exit(1)

filepath = filepath + "/" + nme.replace(" ", "-") + ".desktop"

# Does the .desktop file already exist
print(" -> Prexisting application?")
if (os.path.isfile(filepath)):
    print("Application at `" + filepath + "` already exists. Would you like to procede anyway?", file=sys.stderr, end=" [Y/n]: ")
    ans = input("")
    if (ans.upper() in "Y" or ans == ""):
        pass
    elif (ans.upper() in "N"):
        exit(0)

# Does the executable exist?
print(" -> Executable exists?")
if (not os.path.isfile(exe)):
    print(exe + " does not exist.", file=sys.stderr)
    exit(1);

# Does the executable icon exist?
print(" -> Icon exists?")
if (not os.path.isfile(ico)):
    print(ico + " does not exist.", file=sys.stderr)
    exit(1)

print("-> Generating .desktop file....")
final = template.replace("$(TYPE)", typ).replace("$(NAME)", nme).replace("$(DESC)", des).replace("$(ICON)", ico).replace("$(EXEC)", exe).replace("$(TERM)", trm).replace("$(TAGS)", ';'.join(tags))

print("-> Generated! See .desktop below.")
print(final)

print("-> Saving to `" + filepath + "`....")
with open(filepath, "w") as f:
    f.truncate(0)
    f.write(final)
    f.close()

print("-> Done! Note: you may have to restart your Free Desktop environment (e.g. GNOME).")
