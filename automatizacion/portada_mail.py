#!/usr/bin/python3

import sys
import re

verbosity=1

if verbosity:
    print(sys.argv)

if(len(sys.argv)!=3):
   print("""
Usage:
%s <input directory> <output file>
"""
         % (sys.argv[0]) )

input_dir = sys.argv[1]
output_file = sys.argv[2]

index_hml = input_dir + "/index.html"
sidebar_hml = input_dir + "/sidebar.html"
header_hml = input_dir + "/header.html"

f_index = open(index_hml, "r")
f_sidebar = open(sidebar_hml, "r")
f_header = open(header_hml, "r")

f_output = open(output_file, "w")

ignore_line = False
ignore_script = False
for line in f_index.readlines():
    if not ignore_line and not ignore_script:
        f_output.write(line)
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
            f_output.write(sidebar_line)
        ignore_line = True


    regexp = "\s*<!--\s*HEADER"
    if(re.search(regexp, line)):
        if verbosity:
            print(line)
        for header_line in f_header.readlines():
            f_output.write(header_line)
        ignore_line = True

    regexp = "\s*<script"
    if(re.search(regexp, line)):
        if verbosity:
            print(line)
        ignore_script = True

f_index.close()
f_sidebar.close()
f_header.close()
f_output.close()
