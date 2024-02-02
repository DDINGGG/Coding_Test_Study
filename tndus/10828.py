#스택
#python 3.10이후 버전부터 가능

import sys

n=int(sys.stdin.readline())
lst=[]
    
for i in range(n):
  order= sys.stdin.readline().split()
  k =len(lst)
  match order[0]:
    case 'push':
      lst.append(int(order[1]))
    case 'top':
      if k==0:
        print(-1)
      else:
        print(lst[k-1])
    case 'size':
      print(k)
    case 'empty':
      if k==0:
        print(1)
      else:
        print(0)
    case 'pop':
      if k==0:
        print(-1)
      else:
        print(lst.pop())