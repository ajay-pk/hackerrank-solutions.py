n = int(input())
s = set(map(int, input().split()))
m=int(input())
lst=list()
for _ in range(m):
    lst.append(input().split())
for i in range(len(lst)):
     if lst[i][0]=='pop':
         s.pop()
     elif lst[i][0]=='remove':
         s.remove(int(lst[i][1]))
     elif lst[i][0]=='discard':
         s.discard(int(lst[i][1]))
if len(s)!=0:
    print(*s)
else:
    print('0')

