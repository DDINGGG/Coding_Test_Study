n=int(input())
stack=[]

for _ in range(n):
  try:
    k=list(input().split())
    if k[0]=='push':
      stack.append(k[1])
    elif k[0]=='pop':
      print(stack[len(stack)-1])
      stack.pop()
    elif k[0]=='size':
      print(len(stack))
    elif k[0]=='empty':
      if len(stack)==0:
        print(1)
      else:
        print(0)
    else:
      print(stack[len(stack)-1])
  except:
    print(-1)