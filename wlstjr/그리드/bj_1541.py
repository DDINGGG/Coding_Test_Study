#잃어버린 괄호 siver2
import sys
import re
a,b,c  = []

sik=sys.stdin.readline().split('-')

total=0

for i in sik[0].split('+'):
    total+=int(i)

for i in sik[1:]:
    for j in i.split('+'):
        total-=int(j)

print(total)










# digit = []
# op = []
# word =''
# for i in n:
#     if i.isdigit(): # 문자열에 숫자로만 있으면 True, 하나라도 문자가 있으면 False
#         word += i
#     else:
#         digit.append(int(word))
#         word =''# 숫자를 저장하는 문자열 초기화
#         op.append(i)
# print(digit, op)
     

