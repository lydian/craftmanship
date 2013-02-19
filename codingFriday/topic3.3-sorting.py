def sort(A, B):
    i_A = len(A) -1
    i_B = len(B)-1
    A.extend(['']* len(B))
    index = len(A)  -1
    while i_A >=0 and i_B >=0:
        if B[i_B] > A[i_A]:
            A[index] = B[i_B]
            index -=1
            i_B -= 1
        elif A[i_A] > B[i_B]:
            A[index] = A[i_A]
            index -= 1
            i_A -= 1
        else:
            A[index] = A[i_A]
            A[index -1] = B[i_B]
            index -= 2
            i_A -= 1
            i_B -= 1
    if i_A >=0:
        A[0:index+1] = A[0:i_A+1]
    else:
        A[0:index+1] = B[0:i_B+1]
    return A




A = [1, 3, 5, 7]
B = [2, 4,6]
print sort(A,  B)
A = []
B = [1]
print sort(A,  B)
A = [1]
B = [2, 3, 4, 5, 6]
print sort(A,  B)
A = [1,2,3]
B = [2,5,6]
print sort(A,  B)

