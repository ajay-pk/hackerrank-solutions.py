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
final_list.sort()
for i in range(len(final_list)):
     if i < len(final_list)/2:
             llist.append(final_list[i])
     else:
             uplist.append(final_list[i])
llistl=len(llist)
uplistl=len(uplist)

if uplistl%2==0 and llistl%2==0:
      x=llistl//2
      y=llistl//2-1
      medl= (llist[x]+llist[y])/2
      a=uplistl//2
      b=uplistl//2-1
      medu = (uplist[a]+uplist[b])/2
      
     
      print(float(medu-medl))

elif llistl%2==0 and uplistl%2!=0:
      x=llistl//2
      y=llistl//2-1
      medl= (llist[x]+llist[y])/2
      a=uplistl//2
      medu = uplist[a]
    
      print(float(medu-medl))
elif llistl%2!=0 and uplistl%2==0:
      x=llistl//2
      
      medl= llist[x]
      a=uplistl//2
      b=uplistl//2-1
      medu = (uplist[a]+uplist[b])/2
     
      print(float(medu-medl))

else :
      x=llistl//2
      
      medl= llist[x]
      a=uplistl//2
      medu = uplist[a]
    
      print(float(medu-medl))