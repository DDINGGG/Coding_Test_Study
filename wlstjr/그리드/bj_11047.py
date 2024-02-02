#동전 0 silver4

import sys

N,K = map(int, sys.stdin.readline().split())
coin_type = []
for i in range(N):
    coin_type.append(int(sys.stdin.readline()))
    count = 0
coin_type.reverse()

for i in coin_type:

    count += K//i 
    K%=i
print(count)

#수연 풀이
# n,k=map(int,input().split())
# lst=[]
# for i in range(n):
#   lst.append(int(input()))
# lst.reverse()
# result=0
# for i in lst:
#   result+= k//i
#   k%=i

# print(result)