import sys



n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    cmd = sys.stdin.readline()
    cmd = cmd.split()
    stack_size = len(stack)
    if 'push' in cmd:
        stack.append(int(cmd[1]))
    if 'pop' in cmd:
        if stack_size ==0:
            print(-1)
        else:
            print(stack.pop())
    if 'size' in cmd:
        print(stack_size)

    if 'empty' in cmd:
        if stack_size ==0:
            print(1)
        else:
            print(0)
    if 'top' in cmd:
        if stack_size == 0:
            print(-1)
        else:
            print(stack[-1])

