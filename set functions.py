n=int(input())
s1=set(map(int,input().split()))
m=int(input())
lst=list()
def intersection_update(x,s1):
        
        s1=s1.intersection_update(x)
        print(s.sum())
def symmetric_difference_update(x,s1):
        
        s1=s1.symmetric_difference_update(x)
        print(s.sum())
def update1(x,s):
        
        s1=s1.update(int(x))
        print(s.sum())

def difference_update(x,s):
        s1=s1.difference_update(int(x))
        print(s.sum())
for i in range(m):
    s=[]
    s=list(map(str,input().split()))
    s[1]=int(s[1])
    if s[0]=="intersection_update":
        intersection_update(s[1],s1)
    elif s[0]=="symmetric_difference_update":
        symmetric_difference_update(s[1],s1)
    elif s[0]=="update":
        update1(s[1],s1)
    elif s[0]=="difference_update":
        difference_update(s[1],s1)

