def replace(s, i, r):
    return s[0:i] + r + s[i+1:]

def test(s, p):
    i = 0
    j = 0
    flag = 0
    i= len(s) -1
    while i>=0:
        k = i
        for j in range(len(p)-1, -1, -1):
            if s[k] == p[j] or s[k] == '?':
                k -= 1 
                flag = 1
            else:
                flag = 0
                break
        m = i 
        if flag == 1:
            for j in range(len(p)-1, -1, -1):
                if s[m] == '?':
                    s = replace(s, m, p[j])
                m -= 1
        else:
            if s[i] == '?':
                s = replace(s, i, 'A') 
        i -= 1
    print s

test("ABAAMA????MAZON????????", "AMAZON")
test("?????", "ABCD")
test("CD?????EF", "CDEF")
