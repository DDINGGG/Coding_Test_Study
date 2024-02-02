import sys

n = int(sys.stdin.readline())

def pibo(n):
    if n<=1:
        return n
    else:
        return pibo(n-1) + pibo(n-2)
    
print(pibo(n))

k = [1,2,3,5]

k[2] = 4
print(k)


