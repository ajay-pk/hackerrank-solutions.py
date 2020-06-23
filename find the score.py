import re
n=int(input())
lst=[]
x=[]
for _ in range(n):
    lst.append(str(input().split()))

for i in lst:
     i.split()

     x.append(re.findall("=",i))
x=list(filter(None, x))
count=0
for i in x:
    count+=len(i)
print(count)
     
