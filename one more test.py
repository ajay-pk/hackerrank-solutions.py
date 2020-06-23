def diagonalDifference(arr):
    sumL=0
    sumR=0
    diff=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                sumL+=arr[i][j]
            if i+j==2:
                sumR+=arr[i][j]
    diff=abs(sumL-sumR)
    return diff


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)
