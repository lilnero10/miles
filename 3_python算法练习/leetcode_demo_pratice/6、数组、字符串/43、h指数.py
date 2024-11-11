"""
h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，
并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个
"""
class Solution(object):
    def hIndex(self, citations):
        # 对引用次数数组进行排序
        citations.sort(reverse=True)
        # print(citations)
        h = 0
        # 反向遍历排序后的数组，找到最大的 h 值
        for i, c in enumerate(citations):
            print(f"Index: {i}, Value: {c}")
        #     if c >= i + 1:
        #         h = i + 1
        #         print(i,c)
        #     else:
        #         break
        # return h

# 示例用法
citations1 = [3, 0, 6, 1, 5]
print(Solution().hIndex(citations1))
# citations2 = [1, 3, 1]
# print(Solution().hIndex(citations2))  # 输出: 1