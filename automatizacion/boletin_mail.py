#!/usr/bin/python3

import sys
import re
import tempfile
from urllib.request import urlopen

verbosity=False
boletin = "22"

#web_root = "https://XXX"
web_root = "https://www.sema.org.es/images/boletines/boletin%s/%s" % (boletin, boletin)
#web_root = "https://boletinsema.github.io/boletin22"

if verbosity:
    print(sys.argv)

if(len(sys.argv)!=3):
   print("""
Usage:
%s <input directory> <output file>
"""
         % (sys.argv[0]) )
   sys.exit(1)

input_dir = sys.argv[1]
output_file = sys.argv[2]

# 0. Insertar cabecera html en output_file


index_hml = input_dir + "/index.html"
sidebar_hml = input_dir + "/sidebar.html"
header_hml = input_dir + "/header.html"

# 1. Crear una página htmL autocontenida (sin usar páginas externas) y
# eliminar scripts

f_index = open(index_hml, "r")
f_sidebar = open(sidebar_hml, "r")
f_header = open(header_hml, "r")

f_tmp = open("/tmp/temporalXXX.txt", "w+") #tempfile.TemporaryFile("w+")
f_output = open(output_file, "w")

ignore_line = False
ignore_script = False
insert_CSS=False
for line in f_index.readlines():

    if insert_CSS:
        #Buscar CSS
        regexp = '\s*<link rel="stylesheet"\s*.*\s*href="(https?://.+)"'
        res = re.match(regexp,line)
        if (res):
            css = urlopen(res.group(1))
            style = css.read().decode("utf8")
            f_tmp.write("<style>\n"+style+"\n</style>")
            continue

    if not ignore_line and not ignore_script:
        f_tmp.write(line)
    elif ignore_line:
        ignore_line = False
    else:
        regexp = "\s*</script"
        if(re.search(regexp, line)):
            if verbosity:
                print(line)
            ignore_script = False

    regexp = "\s*<!--\s*SIDEBAR"
    if(re.search(regexp, line)):
        if verbosity:
            print(line)
        for sidebar_line in f_sidebar.readlines():
            f_tmp.write(sidebar_line)
        ignore_line = True

    regexp = "\s*<!--\s*HEADER"
    if(re.search(regexp, line)):
        if verbosity:
            print(line)
        for header_line in f_header.readlines():
            f_tmp.write(header_line)
        ignore_line = True

    regexp = "\s*<script"
    if(re.search(regexp, line)):
        if verbosity:
            print(line)
        ignore_script = True

f_index.close()
f_sidebar.close()
f_header.close()

# 2. Eliminar referencias locales

f_tmp.seek(0)
for line in f_tmp.readlines():

    # Subst local href by global web url
    input_re = '<a href="((\w|-|/)+\.\w+)"'
    output_re = '<a href="' + web_root + '/' + r'\1' + '"'

    result= line
    if(re.search(input_re, line)):
        if verbosity:
            print("   ...found <a href=")
        result = re.sub(input_re, output_re, line)    # Replace a string with a part of itself

    # Sust img src (maybe in the same line!)
    input_re = '<img src="((\w|-|/)+\.\w+)"'
    output_re = '<img src="' + web_root + '/' + r'\1' + '"'
    if(re.search(input_re, result)):
        if verbosity:
            print("   ...found <img src=")
        result = re.sub(input_re, output_re, result)    # Replace a string with a part of itself
    if verbosity:
        print(result)

    # Save to file

    f_output.write(result)


#    print(result)


f_tmp.close()
f_output.close()
