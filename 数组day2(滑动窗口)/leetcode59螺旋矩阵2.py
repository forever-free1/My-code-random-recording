DIRS = (0,1),(1,0),(0,-1),(-1,0) #右下左上
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0]*n for _ in range(n)]
        i = j = di = 0
        for val in range(1,n * n + 1):
            ans[i][j]
            x,y = i + DIRS[di][0] , j + DIRS[di][1] #下一步的位置
            if x < 0 or x >= n or y < 0 or y >= n or ans[x][y]: #如果下一步的位置到界外或有数字就向右旋转90度
                di = (di + 1) % 4  #01230123
            i += DIRS[di][0]
            j += DIRS[di][1]
        return ans