def findforOne(B):
    if len(B) % 2 ==0:
        return (B[len(B)/2] + B[len(B)/2+1])/2
    else:
        return B[len(B)/2+1]

def find(A,B):
    if len(A) == 0 :
        return findforOne(B)
    elif len(B) == 0:
        return findforOne(A)

    #len(A) + len(B) / 2
    max_find = (len(A) + len(B))/2 + 1
    find_one = True
    if(len(A) + len(B) ) % 2 == 0:
        find_one == False

    ia = len(A) /2
    ib = len(B) /2

    defined = 0
    c = [''] * (len(A) + len(B))
    while defined < max_find:
        if A[ia] > B[ib]:
            de
            fined = ib + ia
            c[ defined ] = A[ia] 

            ia = (ia + len(A))/2
            ib += 1
        else:
            defined = ib + ia
            c[defined ] = B[ib]
            
            ia += 1
            ib = (ia + len(B)) /2

            last = B

  
    



A = [ 1, 2, 3]
B= [ 1, 2]
find(A, B)
