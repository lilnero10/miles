"""
路由装饰器
"""
# 路由列表
func_list = {}

# 路由装饰器，让每个函数自动向路由列表中添加数据
def route(data): # data=>/index.html
    def func_outter(func): # func => index
        # 添加数据
        func_list[data] = func_list
        def func_inner():
            pass
        return func_inner
    return func_outter

@route("/index.html") # 1.@func_out  2.index = func_out(index)
def index():
    # 读取路径里的模版数据，返回给浏览器进行渲染
    with open ("./static/index.html") as f:
        file_data = f.read()
    # 模版中的数据替换
    context = file_data.replace("","",1)

    return context

@route("/center.html")
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