def findMax(array):
    sum = 0
    result = []
    for i, list in enumerate(array):
        result.append([])
        for j, value in enumerate(list):
           sum += value
           result[i].appendsum)   
           if sum < 0: 
               sum = 0


    return result
def create2d(dimension, list):
    array = []
    small = []
    for i, v in enumerate(list):
        if i>0 and i % dimension ==0:
            array.append(small)
            small = []
        small.append(v)
        if i == len(list)-1:
            array.append(small)
    return array

print findMax(create2d(4, [0, -2, -7, 0, 9, 2, -6, 2, -4, 1, -4, 1, -1, 8, 0, -2]))
