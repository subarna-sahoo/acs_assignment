from functools import  reduce

def main(K):
    for N in range(10**(K-1), 10**K-1):
        prod_k =  reduce(lambda a,b:int(a)*int(b), list(str(N)))
        sum_k = reduce(lambda a,b:int(a)+int(b), list(str(N)))
        if prod_k >= sum_k:
            return N # first smallest number


if __name__=='__main__':
    K = int(input()) # digits
    if 1 <= K <= 100000:
        print(main(K))
    else:
        print("Not in Constraints")
    
