class Solution:
    # 动态规划算法
    def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        for col in range(n2 + 1):
            dp[0][col] = True

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]


    # 双指针
    def isSubsequence2(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            # print(i, j)
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)