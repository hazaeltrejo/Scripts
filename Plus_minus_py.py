#!/bin/python3

import math
import os
from posixpath import sep, split
import random
import re
import sys

def plusMinus(arr):
    pos=0,
    neg=0
    zero=0
    for i in range (0,len(arr)):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else:
            zero+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zero/len(arr))
input("introduce el arreglo, ejemplo >> 1,0,1,-1,-1,0 \n")
arr=list(map(int, input().rstrip().split(",")))
print(arr)
plusMinus(arr)