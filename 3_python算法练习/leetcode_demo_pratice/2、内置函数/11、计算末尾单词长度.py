class Solution(object):
    def length_of_last_word(self,s):
        # 去除字符串两端的空格
        s = s.strip()

        # 从右向左找到第一个空格，然后计算长度
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            length += 1

        return length

#最简单方法
    def easy_length_of_last_word(self,s):
        return len(s.split()[-1])


s = "   fly me   to   the moon  "
s1 = Solution()
print(s1.length_of_last_word(s))