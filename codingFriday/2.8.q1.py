# assume a1<= a2 <= a3...
def find(A):
    i = 0
    j = i+1
    m = -1
    while i < len(A) and j < len(A):
        if A[i] <= A[j]:
            i+= 1
            j+= 1
            continue
        
        if A[i] > A[j]:
            t = i-1
            while t >=0:
                if A[j] >= A[t]: 
                    if(m <0 or t+1 < m ):
                        m = t + 1
                    n = j
                    print m, n
                    break
                t -= 1    
            j += 1 
    return m, n

A = [1, 2,  3, 5, 4, 2, 6, 4]
#       1, 1, 2, -1 ,-2
#       1, 2, 4,  3,  1
print find(A)
