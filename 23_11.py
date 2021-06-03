n = int(input())
arr = []
for i in range (0,n):
    s = int(input())
    arr.append(s)
def giatribop(arr,i):
    a = 0
    if i == len(arr) - 1:
        a = arr[len(arr)-2] * arr[len(arr)-1]
        return a
    if i == 0:
        a = arr[i] * arr[i+1]
        return a
    a = arr[i] * arr[i+1] * arr[i-1]
    return a
def bt():
    max_ = 0
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    for i in range(len(arr)):
        get = giatribop(arr,i)
        x = arr.pop(i)
        max_ = max(max_,get + bt())
        arr.insert(i,x)
    return max_
print(bt())



     