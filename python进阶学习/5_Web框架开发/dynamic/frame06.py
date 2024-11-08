"""
页面显示数据库内数据
"""
import pymysql
import json
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

    # 创建链接
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="010920hei",
                           db="mydb_1",
                           charset="utf8")

    cursor = conn.cursor()
    sql = "select * from;"
    cursor.execute(sql)
    # 获取数据
    stock_data = cursor.fetchall()

    template = """
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="#ta" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
        """
    html = ''
    for data in stock_data:
        html += template%(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

    # 模版中的数据替换
    context = file_data.replace("{%context%}",html,1)

    cursor.close()
    conn.close()

    return context

@route("/center.html")
def center():
    # 读取路径里的模版数据，返回给浏览器进行渲染
    with open("./static/center.html") as f:
        file_data = f.read()
    # 模版中的数据替换
    context = file_data.replace("", "", 1)

    return context

@route("/center_data.html")
def center_data():
    # 创建链接
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="010920hei",
                           db="mydb_1",
                           charset="utf8")

    cursor = conn.cursor()
    sql = "select"\
        "info.code, info.short, info.chg, info.turnover, info.price, info.highs, focus.note_info"\
        "from info inner join focus on info.id=focus.id;"
    cursor.execute(sql)
    # 获取数据
    stock_data = cursor.fetchall()
    # 把元祖数据转换成列表格式
    center_data_list = [{
                            "code": row[0],
                            "short": row[1],
                            "chg": row[2],
                            "turnover": row[3],
                            "price": row[4],
                            "highs": str(row[5]),
                            "note_info": row[6],
                        }for row in stock_data]
    # 生成json格式的字符串
    json_str = json.dumps(center_data_list)

    cursor.close()
    conn.close()
    return json_str


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