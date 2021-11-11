#!/usr/bin/python

import glob

#list of new functionals
funcs = [ ]

files = glob.glob("[ur]dft*.inp.temp")

for f in files:
  out = open(f,"r").read()
  for func in funcs:
    funct = func.replace("/","d").replace("*", "s")
    open("functionals_dft/" + f.replace("TEMP", funct).replace(".temp",""), "w").write(out.replace("%TEMP%",func))


files = glob.glob("[ur]td*.inp.temp")

for f in files:
  out = open(f,"r").read()
  for func in funcs:
    funct = func.replace("/","d").replace("*","s")
    open("functionals_tddft/" + f.replace("TEMP", funct).replace(".temp",""), "w").write(out.replace("%TEMP%",func))