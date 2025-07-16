class Solution:
    def isHappy(self, n: int) -> bool:
        rec = set()
        while n not in rec:
            rec.add(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num += int(i)**2
            if new_num ==1:
                return True
            else:
                n = new_num
        return False