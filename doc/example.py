#!/usr/bin/env python3

from matplotlib import pyplot as plt
a = [1,2,3]

#>  = new block

#<
#    = dump variables
b = [5,2,4]

>'this becomes a print statement'

#> another block begins here

def main():
    print(a)
    plt.plot(a,b)
    plt.show()

if __name__ == "__main__":
    main()
