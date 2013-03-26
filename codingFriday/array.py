def find(array):
    existed = set()
    for i in array:
        if i not in existed:
            existed.add(i)
        else:
            return i
