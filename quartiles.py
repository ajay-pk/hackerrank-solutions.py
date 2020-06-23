n=input()
item=[]
freq=[]
final_list=[]
count=0
item=list(map(int,input().split()))
freq=list(map(int,input().split()))
for i in freq:
    

    for j in range(1,i+1):
        final_list.append(item[count])
    count=count+1
llist=[]
uplist=[]
lst=final_list.sort()
lst.sort()
if n% 2 == 0:
      if (n/2) %2==0:
          llist=[]
          uplist=[]
          nm=(n//2)-1
          nl=n//2
          med= (lst[nl]+lst[nm])/2
          for i in range(n):
              if i < n/2:
                  llist.append(lst[i])
              else:
                  uplist.append(lst[i])
          llistl=len(llist)
          uplistl=len(uplist)
          x=llistl//2
          y=llistl//2-1
          medl= (llist[x]+llist[y])/2
          a=uplistl//2
          b=uplistl//2-1
          medu = (uplist[a]+uplist[b])/2
          print(float(medu-medl))
      else:
          llist=[]
          uplist=[]
          nm=(n//2)-1
          nl=n//2
          med= (lst[nl]+lst[nm])/2
          for i in range(n):
              if i < n/2:
                  llist.append(lst[i])
              else:
                  uplist.append(lst[i])
          llistl=len(llist)
          uplistl=len(uplist)
          x=llistl//2
          y=uplistl//2
          medl=llist[x]
         
          medu=uplist[y]
          print(float(medu-medl))


                  

       
else:
       
       inew=int(n/2)
       uplist=[]
       llist=[]
       for i in range(0,n-1):
           
           
           if i< inew:
               llist.append(lst[i])
           else:
               uplist.append(lst[i])
           
       llistl=len(llist)
       uplistl=len(uplist) 
       nl=llistl//2
       nu=nl+1
       medL=(llist[nl-1]+llist[nu-1])/2
       nl1=uplistl//2
       nu1=nl1-1
       medU=(uplist[nl1+1]+uplist[nu1+1])/2

       print(float(medu-medl)