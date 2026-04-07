class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapS = {}
        c = 0
        
        mapT = {}
        C = 0

        for i in s:
            if i.isalpha:
                mapS[i] = c
                c + 1
        
        for i in reversed(t):
            if i.isalpha:
                mapT[i] = C
                C + 1

        if mapS == mapT:
            return True
        else:
            return False