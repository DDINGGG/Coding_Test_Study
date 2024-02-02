#전자레인지 bronze 3
#5분 1분 10초 단위로 최소 횟수 구하기

import sys
T = int(sys.stdin.readline())
if T % 10 != 0:
    print(-1)
else:
    five_result = one_result = ten_result = 0 # 결과 변수 초기화
    
    five_result = T // 300 
    one_result = (T % 300)//60
    ten_result = (T % 300) % 60 // 10

    print(five_result, one_result, ten_result)

#수연 풀이
# n=int(input())
# time=[300,60,10]

# if n%10 !=0:
#   print(-1)
# else:
#   for i in time:
#     print(n//i,end=" ")
#     n%=i