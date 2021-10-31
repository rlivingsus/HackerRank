#!/usr/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input("Type a Number:").strip())
    if 1 <= n <= 100:
        if (n % 2) == 0 :
            if (2 <= n <= 5):
                print ("the number is even and between 2 and 5 and Not Weird")
            elif (6 <= n <= 20):
                print ("the number is even and between 6 and 20 and Weird")
            else:
                print ("the number is even and greater than 20 but less than 102")
        else:
            print ("The number is Odd and Weird")
