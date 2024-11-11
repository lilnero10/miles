"""
示例 1：
输入：word1 = "abc", word2 = "pqr"
输出："apbqcr"
解释：字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r
"""
class Solution():

 def merge_words(self,word1,word2):
    merged_word = ''
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            merged_word += word1[i]
        if i < len(word2):
            merged_word += word2[i]
    return merged_word

solution = Solution()

print(solution.merge_words("abcsfadsf","qwers"))

