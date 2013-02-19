#http://www.careercup.com/question?id=1525973##5

#s = "ABAAMA?#???MAZON????????"
#p = "AMAZON"
def rep( s, p ):
    p_i = 0
    solutions = []
    current_solution = {}
    for i, c in enumerate(s):
        if c == p[p_i]:
            p_i+= 1
        elif c == '?':
            current_solution[i] = p[p_i]
            p_i += 1

        elif c != p[p_i]:
            current_solution = {}
            p_i = 0

        if p_i == len(p)-1:
            solutions.append(current_solution)
            p_i = 0 
            current_solution = {}

    print solutions 
        r = ''
        for i,c in enumerate(s):
            if c == '?':
                r += solution[i]
            else:
                r += c
        print r

s = "ABAAMA????MAZON????????"
p = "AMAZON"
rep(s, p)
                


