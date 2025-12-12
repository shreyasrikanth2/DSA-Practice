def findmin(arr):
    minele=arr[0]
    n=len(arr)-1
    for a in range(n):
        if minele>arr[a]:
            minele=arr[a]
    return minele
print(findmin([3, 5, 4, 1, 9]))
