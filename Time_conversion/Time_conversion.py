#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    time = int(s[:2])
    msec = s[2:8]
    time = time % 12 if s[-2:] == 'AM' else time % 12 + 12
    return f"{time}{msec}"

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result,"\n")

