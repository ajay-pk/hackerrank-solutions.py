import re
n=int(input())
s=[]
for _ in range(n):
    s.append(str(input()))
pattern="\A\+?-?(\d+)?\.\d+\Z"
for i in s:
    if re.match(pattern,i):
        print(True)
    else:
        print(False)
