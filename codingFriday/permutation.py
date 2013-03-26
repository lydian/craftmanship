
def permutation( topic, current):
    if len(current) == len( topic):
        print current
        return

    unused = set(topic) - set(current)
    for ch in unused:
        permutation(topic, current + ch)

permutation("ABCD", "")
