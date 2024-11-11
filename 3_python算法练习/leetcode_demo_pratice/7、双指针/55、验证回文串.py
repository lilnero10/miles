"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个回文串
"""

def is_palindrome(s: str) -> bool:
    # 将所有字符转换为小写，并保留字母和数字字符
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    # 检查过滤后的字符是否是回文
    return filtered_chars == filtered_chars[::-1]

# 示例
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))  # 输出: True