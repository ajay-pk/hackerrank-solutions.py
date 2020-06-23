

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
if n in range(10,2500):
    for i in range(0, n): 
       ele = int(input()) 
  
       lst.append(ele) # adding the element 
    
    print("{:.1f}".format(sum(lst)/n),) #mean
    lst.sort()
    if n% 2 == 0:
       nn=n//2
       nm=nn-1
       med=(lst[nn]+lst[nm])/2
       print("{:.1f}".format(med) )#median
       
    else:
       new=int(n/2)
       print(lst[new])

    newlist={}   # saves counts
    for item in lst:
      newlist[item]=lst.count(item)
    ans=()
    ans=max(newlist.values())
    for key,value in newlist.items():
        if value==ans:
            print(key)
            break
       
       
