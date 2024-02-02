#세탁소 사장 동혁 Bronze3
#input : test case T and type int C(cent)
#output : quarter dime nickel penny

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    count =0 
    C = int(sys.stdin.readline())
    quarter = dime = nickel = penny = 0

    quarter = C//25
    dime = (C%25)//10
    nickel = (C%25)%10//5
    penny = (C%25)%10%5//1

    print(quarter, dime, nickel, penny)    
       
    
    
