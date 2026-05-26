class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFinal = "".join(sorted(s))
        tFinal = "".join(sorted(t))

        if sFinal == tFinal:
            return True
        else:
            return False
