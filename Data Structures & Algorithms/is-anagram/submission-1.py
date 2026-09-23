class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {chr(i): 0 for i in range(97, 123)}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] +=1
            if t[i] in count:
                count[t[i]] -=1
        if  not any (count.values()):
            print(count)
            return True
        else:
            return False