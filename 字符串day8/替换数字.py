#给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。

#例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。

class Solution(object):
    def subsitute_numbers(self, s):
        result = []
        for i in s:
            if '0' <= i <= '9':
                result.append('number')
            else:
                result.append(i)
        return ''.join(result)
 
if __name__ == "__main__":
    solution = Solution()
 
    while True:
        try:
            s = input()
            result = solution.subsitute_numbers(s)
            print(result)
        except EOFError:
            break