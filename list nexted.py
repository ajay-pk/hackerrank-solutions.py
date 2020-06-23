n=int(input())
lst1=[]
lst=[]
for i in range(n):
    lst1.append((input().split()))

for functioncall in lst1:
    
     if functioncall[0]=='insert':
          lst.insert(int(functioncall[1]),int(functioncall[2]))
        
        
        
     elif functioncall[0]=='print':
          print(lst)
        
            
     elif functioncall[0]=='remove':
          lst.remove(int(functioncall[1]))
         
     elif functioncall[0]=='append':
          lst.append(int(functioncall[1]))
        
     elif functioncall[0]=='sort':
          lst.sort()
        
     elif functioncall[0]=='pop':
          lst.pop()
        
     elif functioncall[0]=='reverse':
          lst.reverse()
        

