import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip()) 

def bestdivisorofn(n):
    factor_list = []
    for fac1 in range(1, (n//2)+1): 
        if n%fac1 == 0: 
            fac2 = n//fac1 
            f1 = sum(list(map(int, str([fac1][0])))) 
            f2 = sum(list(map(int, str([fac2][0]))))    
            factor_list.append(max(f1, f2))
        else:
            pass  
    return max(factor_list) 
#testig 
bestdivisorofn(24)