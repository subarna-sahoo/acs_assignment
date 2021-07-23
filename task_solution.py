"""
# Task

You are given an integer K.

Write code to determine a valid integer having K digits such that 
the product of digits of the integer is greater than or equal to 
the sum of digits of the integer and the product of the digits of 
the integer is minimized. If more than 1 such integer exists, 
determine the smallest possible integer.
"""

from functools import  reduce

def main(K):
    for N in range(10**(K-1), 10**K-1):
        prod_k =  reduce(lambda a,b:int(a)*int(b), list(str(N)))
        sum_k = reduce(lambda a,b:int(a)+int(b), list(str(N)))
        if prod_k >= sum_k:
            return N # first smallest number


if __name__=='__main__':
    K = input() # digits
    if 1 <= K <= 100000:
        print(main(K))
    else:
        print("Not in Constraints")
    
