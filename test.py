
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
n=len(final_list)
def med1(arr):
    arr.sort()
    if len(arr) % 2 == 1:
        ret_value = arr[int((len(arr)-1)/2)]
    else:
        ret_value = 0.5*(arr[int(len(arr)/2-1)]+arr[int(len(arr)/2)])
    return ret_value

N = len(final_list)



Q2 = med1(final_list)

l_arr = [i for i in final_list if i < Q2]
u_arr = [i for i in final_list if i > Q2]

Q1 = med1(l_arr)
Q3 = med1(u_arr)
print(Q3-Q1)
