n= int(input())
names=[]
score=[]
for i in range(n):
    x= input()
    names.append(x)
    y= float(input())
    score.append(y)
newnames=[]

minimum= min(score)
secmin=100

for i in range(n):
    if score[i]<secmin and score[i]>minimum:
        secmin=score[i]
for i in range(n):
    if secmin==score[i]:
        newnames.append(names[i])
newnames.sort()
print(secmin)
for i in newnames:
    print(i)

