def count(number):
    total = 0
    for i in range(32):
        if number % 2 == 1:
            total += 1
        number /= 2
        if number == 0:
            break
    return total

def count2(number):
    return len([i for i in "{0:b}".format(number)[:32] if i == '1'])


print count(0)
print count2(0)
print count(11)
print count2(11)
print count(20)
print count2(20)
print count(pow(2,32)-1)
print count2(pow(2,32)-1)
