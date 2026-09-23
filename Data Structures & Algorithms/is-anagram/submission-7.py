class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {chr(i): 0 for i in range(97, 123)}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count[s[i]] +=1
            count[t[i]] -=1
        if not any (count.values()):
            return True
        else:
            return False