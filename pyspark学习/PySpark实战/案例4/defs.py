import jieba

def context_jieba(data):
    seg = jieba.cut_for_search(data)
    l = list()
    for word in seg:
        l.append(word)
    return l

def filter_words(data):
    return data not in ['谷', '博', '客']

def append_words(data):
    if data == '传智播':data = '传智播客'
    if data == '院校': data = '院校帮'
    if data == '博学': data = '博学谷'
    return data

def extract_user_and_word(data):
    user_id = data[0]
    context = data[1]

    words = context_jieba(data)

    return_list = list()
    for word in words:
        if filter_words(word):
            return_list.append((user_id + "_" + append_words(word)[0], 1))

        return return_list

# 提取 ID 字段
def extract_id(data):
    parts = data.split()
    return parts[1]  # 第二个字段是 ID

# 定义解析函数
def parse_log_line(data):
    parts = data.split()
    ip = parts[0]
    request_type = parts[3]  # 如 GET 或 POST
    url = parts[4]           # URL
    return (ip, request_type, url)