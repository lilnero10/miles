def index():
    # 读取路径里的模版数据，返回给浏览器进行渲染
    with open ("./static/index.html") as f:
        file_data = f.read()

    return file_data

def center():
    return "center.html"

def error():
    return "404 error"

# 接口
def application(request_path):
    if request_path == "/index.html":
        # 应答体
        # 生产上经过复杂业务处理,再返回页面数据
        return index()
    elif request_path == "/center.html":
        return center()
    else:
        return error()