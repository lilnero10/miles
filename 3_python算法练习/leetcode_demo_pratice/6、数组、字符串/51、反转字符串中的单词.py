class Solution(object):
    def reverse_words(self,s):
        # 去除前导和尾随空格，并按空格分隔字符串
        words = s.strip().split()
        # 反转单词列表
        reversed_words = words[::-1]
        # 用单个空格连接反转后的单词列表
        return ' '.join(reversed_words)

    # 示例测试
    s1 = "the sky is blue"
    s2 = "  hello world  "
    print(reverse_words(s1))  # 输出: "blue is sky the"
    print(reverse_words(s2))  # 输出: "world hello"