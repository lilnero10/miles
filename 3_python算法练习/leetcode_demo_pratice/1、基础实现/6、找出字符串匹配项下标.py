class Solution():
    def strStr(self, haystack, needle):
        return haystack.find(needle)

haystack = "hello"
needle = "ll"
s = Solution()
print(s.strStr(haystack, needle))