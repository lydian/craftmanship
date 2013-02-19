#15011669

def wc(str):
    max = 0
    wcs = {}
    for c in str:
        if c == '': continue
        if c not in wcs:
            wcs[c] = 1
        else:
            wcs[c] += 1
        if wcs[c] > max:
            max = wcs[c]
    return max


print wc("coffee tuffee")
