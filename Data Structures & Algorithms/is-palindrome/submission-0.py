class Solution:
    def isPalindrome(self, s: str) -> bool:
        reS = ''
        for i in s:
            if i.isalnum():
                reS += i.lower()
        return reS == reS[::-1]