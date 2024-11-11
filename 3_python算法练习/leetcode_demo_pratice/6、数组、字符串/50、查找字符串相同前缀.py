class Solution(object):
    def longest_common_prefix(self,strs):
        if not strs:
            return ""

        # 取第一个字符串作为基准
        prefix = strs[0]
        print(strs[1:])

        # 遍历字符串数组
        for s in strs[1:]:
            # 更新前缀
            while not s.startswith(prefix):
                # 缩短前缀
                prefix = prefix[:-1]
                # 如果前缀为空，则返回空字符串
                if not prefix:
                    return ""
        print(prefix[:-1])

        return prefix

# 示例测试
strs = ["flower", "flow", "flight"]
print(Solution().longest_common_prefix(strs))  # 输出: "fl"