"""
输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]
"""

from collections import Counter
def findSubstring(s: str, words: list) -> list:
    if not s or not words:
        return []

    word_len = len(words[0])
    word_count = len(words)
    substring_len = word_len * word_count
    words_counter = Counter(words)
    results = []

    for i in range(len(s) - substring_len + 1):
        seen_words = Counter()
        for j in range(i, i + substring_len, word_len):
            current_word = s[j:j + word_len]
            if current_word in words_counter:
                seen_words[current_word] += 1
                if seen_words[current_word] > words_counter[current_word]:
                    break
            else:
                break
        if seen_words == words_counter:
            results.append(i)

    return results


# 示例使用
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))