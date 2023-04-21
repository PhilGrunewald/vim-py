#!/usr/bin/env python3
import vimpy as vp
locals().update(vp.restore('example.py'))
#_#
from matplotlib import pyplot as plt
#_#a = [1,2,3]
#_#
#_##>  = new block
#_#
#_#vp.printState(locals())
#_##    = dump variables
#_#b = [5,2,4]
#_#
#_#print('this becomes a print statement')
#_#
#> another block begins here

def main():
    print(a)
    plt.plot(a,b)
    plt.show()

if __name__ == "__main__":
    main()
