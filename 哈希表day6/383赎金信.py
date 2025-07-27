class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        cnt = dict()
        for c in magazine:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        
        for c in ransomNote:
            if c not in cnt or cnt[c] == 0:
                return False
            cnt[c] -= 1
        return True