n=int(input())
newlist=[]
if n<51 and n>4:
    x= list(map(int,input().split()))
    w= list(map(int,input().split()))
    for i in range(0,n):
        newlist.append(x[i]*w[i])
        
    s= sum(newlist)
    s1= sum(w)
    ans=s/s1
    print(s,s1)
    print("{:.1f}".format(ans))

        


