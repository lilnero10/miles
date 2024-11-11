from collections import Counter
def minWindow(s: str, t: str) -> str:
    need = Counter(t)  # 记录 t 中字符的数量
    window = {}
    left, right = 0, 0
    valid = 0  # 记录窗口中满足条件的字符数量

    start = 0  # 记录最小子串的起始位置
    min_len = float("inf")  # 记录最小子串的长度

    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 右移窗口
        right += 1
        # 进行窗口内数据的一系列更新
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # 更新最小覆盖子串
            if right - left < min_len:
                start = left
                min_len = right - left

            # d 是将移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1
            # 进行窗口内数据的一系列更新
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    # 返回最小覆盖子串
    return "" if min_len == float("inf") else s[start:start + min_len]