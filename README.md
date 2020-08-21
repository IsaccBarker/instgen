# instgen
Generate a .desktop file for Free Desktop based systems. Developed on my new Arch box.

# running
instgen contains a python shebang line, so just copy it over to your path (e.g. /usr/local/bin). A usage menu will pop up opon running.

```
instgen -- a simple utility in python for generating a .desktop file for an application for free desktop based systems.
    GLOSARY:
        A       :       Application
        L       :       Link
        D       :       Directory
        Y/n     :       Yes / No
        none    :       No icon
        .       :       End List

    USAGE:
        instgen stdin                                                                                                                        ~ Will take arguments from stdin
        instgen Type[A/l/d] Name PathToExecutable PathToIcon Terminal[Y/n] Description Owner(all for all) Tags(; separated string in quotes) ~ Takes arguments from command line
    AUTHOR
        Milo Banks (Copyright 2020 under GNU GPL)
```

# using instgen on instgen (example)
```bash
$ ./instgen.py A instgen instgen.py none y "generate .desktop files" all "Code;Coding;Programming;Program;Software;Install;Installation"
-> Parsing input....
-> Validating environment....
 -> Does appropriate .desktop directory exist?
 -> Prexisting application?
 -> Executable exists?
 -> Icon exists?
-> Generating .desktop file....
-> Generated! See .desktop below.

[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=instgen
Comment=generate .desktop files
Icon=/opt/instgen/instgen.py
Exec=/opt/instgen/instgen.py
Terminal=true
Categories=Code;Coding;Programming;Program;Software;Install;Installation

-> Saving to `/usr/share/applications/instgen.desktop`....
-> Done! Note: you may have to restart your Free Desktop environment (e.g. GNOME).
```
