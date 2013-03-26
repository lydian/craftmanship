def find(arr):
    end = len(arr)
    start = 0
    current = (start + end) /2 
    while current > 0 and current < len(arr)-1:
        if arr[current] > arr [current -1]  and arr[current+1] > arr[current]:
            start = current + 1
        elif arr[current] < arr[current - 1] and arr[current+1] < arr[current]:
            end = current-1
        else:
            return arr[current]
        current = (start + end) / 2

print find([1,2,3,4, 5,8, 9, 10, 9, 7, 2, 1])
