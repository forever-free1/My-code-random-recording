class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rec = [0]*26
        for i in s:
            rec[ord(i)-ord('a')] += 1
        for i in t:
            rec[ord(i)-ord('a')] -= 1
        for i in range(26):
            if rec[i] != 0:
                return False
        return True
        