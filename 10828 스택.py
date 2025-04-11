import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    comm = sys.stdin.readline().strip() 
    if comm.startswith('push'):
        comm = comm.split()
        stack.append(int(comm[-1]))
        
    elif comm == 'top':
        if not len(stack):
            print(-1)
            
        else:
            print(stack[-1])
            
    elif comm == 'size':
        print(len(stack))
        
    elif comm == 'pop':
        if not len(stack):
            print(-1)
            
        else:
            print(stack.pop())
            
    elif comm == 'empty':
        if not len(stack):
            print(1)
            
        else:
            print(0)
