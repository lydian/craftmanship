import re
import unittest
def compare(required, current):
    if len(current) != len(required): return False
    for c in required:
        if current[c] < required[c]: return False
    return True

def minWindow(S, T):
    required = {}
    current = {}
    for c in T:
        if c not in required: required[c] = 0
        required[c] += 1
    
    start = -1
    end = 0
    result = ""
    while end < len(S):
        c = S[end]
        if c in required:
            if c not in current:
                current[c] = 0
            current[c] += 1
            if start == -1:
                start = end

            if compare(required, current):
                if result == "":
                    result = S[start:end+1]
                while start <=end:
                    if S[start] in current and current[S[start]] <= required[S[start]]: break
                    if(S[start] in current): current[S[start]] -= 1
                    start += 1
                if len(result) > len(S[start:end+1]):
                    result= S[start:end+1]
        end += 1

    return result

class Test(unittest.TestCase):
    def test(self):
        f = open("testcase-leet76")
        for line in f:
            S,T,error,expected = [string.strip().replace("\"", "") for string in re.split("[, ]+", line) if string.strip() != ""]
            result = minWindow(S,T)
            self.assertEqual(expected, minWindow(S,T))
        

unittest.main()
