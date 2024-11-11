def find_first_occurrence(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# 示例用法
haystack = "sadbutsad"
needle = "sad"
result = find_first_occurrence(haystack, needle)
print(result)  # 输出: 0