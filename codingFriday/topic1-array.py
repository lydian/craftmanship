
def findMaximum(array):
    result = []
    sum = 0
    last_start = 0
    max_i = 0
    for i, value in enumerate(array):
        sum += value 
        if len(result)>0 and sum > result[max_i]["value"]:
            max_i = i
        result.append({"value": sum, "start": last_start})
        if sum < 0:
            sum = 0 
            last_start = i + 1
    return result[max_i]["value"], array[result[max_i]["start"]: max_i+1]

def showtest(array):
    data = array
    print "input:", data
    print "output:", findMaximum(data)
    print "======"

showtest([1]) 
showtest([-1]) 
showtest([0, 1]) 
showtest([-2, 1, -3, 4, -1, 2, 1, -5 ,4])
showtest([-2, 1, -3, 4, -1, 2, 1, -5 ,4])
showtest([-2, 1, -3, 4, -1, 2, 1, -5 ,4, 3])
showtest([-2, -1, -3, -4, -1, -2, -1, -5 , -1, -1])
showtest([-2, -1, -3, -4, -1, -2, -1, 5 , -1, -1])
showtest([-2, -1, -3, 4, -1, 7, -1, 5 , -1, -1])
