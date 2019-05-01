#!/usr/bin/python3

import sys
import re
import tempfile

verbosity=1
boletin = "21"
web_root = "https://www.sema.org.es/images/boletines/boletin%s/%s" % (boletin, boletin)

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

index_hml = input_dir + "/index.html"
sidebar_hml = input_dir + "/sidebar.html"
header_hml = input_dir + "/header.html"

# 1. Crear una página htmL autocontenida (sin usar páginas externas) y
# eliminar scripts

f_index = open(index_hml, "r")
f_sidebar = open(sidebar_hml, "r")
f_header = open(header_hml, "r")

f_tmp = tempfile.TemporaryFile("w+") # Por defecto, en modo 'w+b' (lectura y escritura)
f_output = open(output_file, "w")

ignore_line = False
ignore_script = False
for line in f_index.readlines():
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
for tmp_line in f_tmp.readlines():

    # Subst local href by global web url
    input = '<a href="(\w+\.\w+)"'
    output = '<a href="' + web_root + '/' + r'\1' + '"'

    result = re.sub(input, output, tmp_line)    # Replace a string with a part of itself
    print(result)

    # Subst local href by global web url
    input = '<img src="(\w*\/*\w+\.\w+)"'
    output = '<img src="' + web_root + '/' + r'\1' + '"'

    result = re.sub(input, output, result)    # Replace a string with a part of itself
    print(result)

    # Save to file

    f_output.write(result)


#    print(result)


f_tmp.close()
f_output.close()
