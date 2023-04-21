#!/usr/bin/env python3
""" input
        1) filename
        2a) line number > process file
        2b) a word > look up and display help

    "#>" start and end of block
         loads variables at start of block
         executes block surrounding current linenumber
         stores the variable state at end of block
    "#<" prints variables
"""
import sys

"""  Comment handling """

def commentOut(lines,n):
    lines[n] = (f"#_#{lines[n]}")
    return lines

def uncomment(lines,n):
    lines[n] = lines[n].replace("#_#","")
    return lines


""" Variable handling """

def restoreImports(lines):
    for n,line in enumerate(lines):
        if line.startswith('#_#from '):
            uncomment(lines,n)
        elif line.startswith('#_#import '):
            uncomment(lines,n)
        elif line.startswith('#_##!/'):
            uncomment(lines,n)
    return lines

def restoreFunctions(lines):
    isFunction = False
    for n,line in enumerate(lines):
        if line.startswith('#_#def '):
            isFunction = True
        elif not line.startswith('#_#    '):
            isFunction = False
        if isFunction:
            uncomment(lines,n)
    return lines


""" output """

def printColour(lines,start,end):
    """ make output look good /green """
    lines.insert(start,"print('\\033[92m', end='')\n")
    lines.insert(end,"print('\\033[0m', end='')\n")
    return lines

def mainHelp(filename,helpStr):
    """ comment out everything, except the line to print help for in .filename """
    with open(filename) as f:
        lines = f.readlines()
    for n in range(len(lines)):
        lines[n] = (f"#_#{lines[n]}")
    lines = restoreImports(lines)
    lines.append(f"print(help({helpStr}))\n")
    with open(f".{filename}","w") as f:
        f.writelines(lines)

def main(filename,linenumber):
    """ open filename, process and write as .filename """
    with open(filename) as f:
        lines = f.readlines()
    blocks = [n for n,line in enumerate(lines) if line.startswith('#>')]
    start = 0
    for block in blocks:
        if block <= linenumber:
            for n in range(block-start):
                lines = commentOut(lines,n+start)
            start = block
        if block > linenumber:
            # comment out to the end
            for n in range(len(lines)-block):
                lines = commentOut(lines,n+block)
            lines.insert(block,(f"vp.store(locals(),'{filename}')\n"))
            lines = printColour(lines,start,block+1)
            break
    if blocks:
        lines = restoreFunctions(lines)
        lines = restoreImports(lines)
        lines.insert(1,(f"locals().update(vp.restore('{filename}'))\n"))
        lines.insert(1,'import vimpy as vp\n')

    lines = [line.replace("#<\n","vp.printState(locals())\n") for line in lines]
    with open(f".{filename}","w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    if sys.argv[2].isdigit():
        main(sys.argv[1],int(sys.argv[2])-1)
    else:
        mainHelp(sys.argv[1],sys.argv[2])
