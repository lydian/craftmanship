def find(A, B, n):
    greater = {}
    while True:
        ia = len(A)/2
        ib = len(B)/2

        if ia + ib > n:
            if A[ia] > B[ib]:
                ib /= 2
            else:
                ia /=2
        if ia + ib < n:
            if A[ia] > B[ib]:
                ib = 3/2 * ib
            else:
                ia = 3/2 * ia

        else:
            return max(A[ia], B[ib])


A = [1, 2, 3, 5, 6,  7]
B = [4, 5]
print find(A,B, 4)
