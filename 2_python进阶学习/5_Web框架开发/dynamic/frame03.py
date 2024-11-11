"""
路由列表，实现需要返回大量页面
"""
# 路由列表
func_list = {}
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

# 向路由列表中添加数据
func_list["./index.html"] = index
func_list["./center.html"] = center
# 列表中的数据
# {
#     "./index.html":index,
#     "./center.html":center
# }

# 接口
def application(request_path):
    try: # 防止读取文件错误抛异常
        func = func_list[request_path]
        # index()
        ret = func()
        # 返回对动态资源的处理结果
        return ret
    except Exception as e:
        return error()