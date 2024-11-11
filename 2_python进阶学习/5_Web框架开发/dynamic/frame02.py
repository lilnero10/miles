"""
替换返回html页面的内容
"""
def index():
    # 读取路径里的模版数据，返回给浏览器进行渲染
    with open ("./static/index.html") as f:
        file_data = f.read()
    # 模版中的数据替换
    context = file_data.replace("","",1)

    return context

def center():
    # 读取路径里的模版数据，返回给浏览器进行渲染
    with open("./static/center.html") as f:
        file_data = f.read()
    # 模版中的数据替换
    context = file_data.replace("", "", 1)

    return context

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