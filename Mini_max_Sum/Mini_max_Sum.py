#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    min_sum=0
    max_sum=0
    arr=sorted(arr)
    for i in range(4):
        min_sum=min_sum+arr[i]
    for j in range(4):
        max_sum=max_sum+arr[len(arr)-(j+1)]
    print(min_sum, max_sum)

input("introduce el arreglo, ejemplo >> 1,0,1,-1,-1,0 \n")
arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)
