#거스름돈 bronze 2

import sys
n=int(sys.stdin.readline())
money=[500,100,50,10,5,1]
count = 0
n = 1000-n
for i in money:
    count += n//i 
    n%=i
print(count)