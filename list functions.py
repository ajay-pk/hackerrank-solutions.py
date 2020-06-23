list=[]
n=int(input())
lst=[]

listoffunctions=[]

for i in range(n):
    listoffunctions.append(input().split())

for i in range(n):
         functioncall=[]
          functioncall.clear()
     
          print(functioncall[0])
    
          if functioncall[0]=='insert':
             lst.insert(functioncall[1],functioncall[2])
             print("insert is working")
          elif functioncall[0]=='print':
              print(lst)
            
          elif functioncall[0]=='remove':
               lst.remove(functioncall[1])
               print("remove is working")
          elif functioncall[0]=='append':
              lst.append(functioncall[1])
              print("append is working")
          elif functioncall[0]=='sort':
              lst.sort()
              print("sort is working")
          elif functioncall[0]=='pop':
              lst.pop()
              print("pop is working")
          elif functioncall[0]=='reverse':
              lst.reverse()
              print("revers is working")


    
