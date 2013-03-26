def reverse(string, start, end):
    j = end -1
    for i in range(start, (start + end)/2):
        temp = string[i]
        string[i] = string[j]
        string[j] = temp
        j -= 1
    return string

def rotate(string, k):
    string = list(string)
    string = reverse(string, 0, len(string))
    string = reverse(string, 0, len(string)-k)
    string = reverse(string, len(string)-k, len(string))
    print "".join(string)

rotate('abcdefg', 3)

