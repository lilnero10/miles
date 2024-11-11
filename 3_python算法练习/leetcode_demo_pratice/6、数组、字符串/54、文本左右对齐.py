def full_justify(words, maxWidth):
    res = []
    current_line = []
    current_length = 0

    for word in words:
        # 检查添加下一个单词是否会达到最大长度
        if current_length + len(word) + len(current_line) > maxWidth:
            for i in range(maxWidth - current_length):
                # 尽可能均匀地分配空间
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            res.append(''.join(current_line))
            current_line, current_length = [], 0
        current_line.append(word)
        current_length += len(word)

    # 处理最后一行：左对齐
    res.append(' '.join(current_line).ljust(maxWidth))
    return res


# 示例用法
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
result = full_justify(words, maxWidth)
for line in result:
    print(f'"{line}"')