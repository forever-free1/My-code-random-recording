class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        for i in range(0,n,k*2):
            s[i:i+k] =s[i:i+k][::-1]
        return ''.join(s) 