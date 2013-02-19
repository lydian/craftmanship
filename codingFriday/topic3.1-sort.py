# merge two sorted array

def merge(arrayA, arrayB):
    a_i = b_i = 0
    result = []
    while a_i < len(arrayA) and b_i < len(arrayB):
        if arrayA[a_i] < arrayB[b_i] :
            result.append(arrayA[a_i])
            a_i += 1
        elif arrayB[b_i] < arrayA[a_i] :
            result.append(arrayB[b_i])
            b_i += 1
        else:
            result.append(arrayA[a_i])
            result.append(arrayB[b_i])
            a_i += 1
            b_i += 1
    return result

print merge([1,3,5,7,9], [2,6,8])
