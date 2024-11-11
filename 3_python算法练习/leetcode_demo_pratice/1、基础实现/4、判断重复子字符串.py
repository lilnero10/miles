def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return True
    return False

s1 = "abab"

print(repeatedSubstringPattern(s1))