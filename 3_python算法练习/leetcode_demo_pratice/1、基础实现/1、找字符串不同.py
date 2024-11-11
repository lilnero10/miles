from collections import Counter

class Solution():
     def findTheDifference(self,s,t):
        return list(Counter(t) - Counter(s))[0]



x = Solution()
s = "asdfg"
t = "asdfgh"
print(x.findTheDifference(s, t))