# sort n sorted array without using extra space
def sortTwo(A, len_A, B):
    index = len_A + len(B)-1
    print index+1
    i_a = len_A -1
    i_b = len(B) -1
    while i_a >=0 and i_b >=0: 
        if A[i_a]  > B[i_b]:
            A[index] = A[i_a]
            index -= 1
            i_a -= 1
        elif A[i_a] < B[i_b]:
            A[index] = B[i_b]
            index -=1
            i_b -= 1
        else:
            A[index] = A[i_a]
            A[index-1] = B[i_b]
            i_a -= 1
            i_b -= 1
            index -= 2
    
    if i_a >=0:
        A[0:index+1] = A[0:i_a+1]
    elif i_b >=0:
        A[0:index+1] = B[0:i_b+1]
    
    return A, len_A + len(B)

def sort(arrays):
    num_array = len(arrays)
    num_elements = reduce( lambda x,y: x+y, [len(array) for array in arrays])
    result = []
    for i in arrays[0]:
        result.append(i)
    result.extend([-1]*(num_elements - len(arrays[0])))
    len_A = len(arrays[0])
    for i in range(1, num_array):
        B = arrays[i]
        result, len_A = sortTwo(result, len_A, B)
    return result

def findMin(arrays, pointers):
    for i, array in enumerate(arrays):
        if pointers[i] != len(array):
            min_i = i
            break

    for i, array in enumerate(arrays):
        if pointers[i] == len(array): continue
        if array[pointers[i]] < arrays[min_i][pointers[min_i]]:
            min_i = i


    return min_i

def sort2(arrays):
    num_array = len(arrays)
    num_elements = reduce( lambda x,y: x+y, [len(array) for array in arrays])
    pointers = [0] * len(arrays)
    result = []
    for i in range(num_elements):
        min_row = findMin(arrays, pointers)
        result.append( arrays[min_row][pointers[min_row]] ) 
        pointers[min_row] += 1

    return result





arrays = [[1,3,4,4], [2,5,8,9], [3,5,9,11], [4,7,8, 10]]
print sort(arrays)
print sort2(arrays)

