#http://www.careercup.com/question?id=14360665
'''
Given two strings .Print all the interleavings of the two strings.
Interleaving means that the if B comes after A .It should also come after A in the interleaved string.
ex-
AB and CD
ABCD
ACBD
ACDB
CABD
CADB
CDAB
'''

def cp(current, strA, strB, lastX, lastY):
    if len(current) == len(strA) + len(strB):
        print current
        return
    for str_i in range(lastX+1, len(strA)):
        cp(current + strA[str_i], strA, strB, str_i, lastY)

    for str_j in range(lastY+1, len(strB)):
        cp(current + strB[str_j], strA, strB, lastX, str_j)    


def permutation(current, remain, usage):
    if len(current) == len(remain):
        print current
        return 
    for str_i in range(len(remain)):
        if usage[str_i]: continue
        str = remain[str_i]
        usage[str_i] = True
        permutation(current+str, remain, usage )
        usage[str_i] = False



#str = "ABCD"
#permutation('', str, [False for i in str] )

strA = "ABE"
strB = "CDF"
cp('', strA, strB, -1, -1)
