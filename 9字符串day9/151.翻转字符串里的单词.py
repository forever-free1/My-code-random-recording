#双指针
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()  # 去除首尾空格
        res = []
        i = j = len(s) - 1
        
        while i >= 0:
            # 1. 找到当前单词前面的第一个空格
            while i >= 0 and s[i] != ' ':
                i -= 1
            # 此时 i 指向空格或 -1
            res.append(s[i+1:j+1])  # 提取单词
            
            # 2. 跳过单词之间的空格
            while i >= 0 and s[i] == ' ':
                i -= 1
            # 此时 i 指向下个单词的最后一个字符
            
            j = i  # j 指向下个单词的尾部
        
        return " ".join(res)

#分割加倒序
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()         # 删除首尾空格
        strs = s.split()      # 分割字符串
        strs.reverse()        # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回

