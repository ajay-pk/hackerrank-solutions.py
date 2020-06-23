nm=[]
nm=list(map(int,input().split()))
array=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happiness=0
for i in A:
    if i in array:
        happiness+=1
for i in B:
    if i in array:
        happiness-=1
print(happiness)