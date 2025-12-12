def findmax(arr):
    maxele=arr[0]
    n=len(arr)-1
    for a in range(n):
        if maxele<arr[a]:
            maxele=arr[a]
    return maxele
print(findmax([3, 5, 4, 1, 9]))
