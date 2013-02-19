#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#For example,
#S = "ADOBECODEBANC"
#T = "ABC"
#Minimum window is "BANC".
#
#Note:
#    If there is no such window in S that covers all characters in T, return the emtpy string "".
#
#    If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

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
        f = open("tests/leetcode-76.data")
        for line in f:
            S,T,error,expected = [string.strip().replace("\"", "") for string in re.split("[, ]+", line) if string.strip() != ""]
            result = minWindow(S,T)
            self.assertEqual(expected, minWindow(S,T))
        
unittest.main()
