class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                flag = True
            return flag
        else:
            return flag

        