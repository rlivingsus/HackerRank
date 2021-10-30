#!/usr/bin/python3

if __name__ == '__main__':
    #print(type(input("Type two numbers: ").split()))
    #used the type function to figure out what the input was returning
    #the input was a list.  Below was used to go through a list and split
    a, b = [int(x) for x in input("Type two numbers: ").split()]
    print (a + b)
    print (a - b)
    print (a * b)
