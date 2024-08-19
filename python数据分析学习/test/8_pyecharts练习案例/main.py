from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

from file_define import FileReader,TextFileReader,JsonFileReader
from data_define import Records

text_file_reader=TextFileReader("数据文件路径")
json_file_reader=JsonFileReader("数据文件路径")

jan_data = text_file_reader.read_data()
feb_data = json_file_reader.read_data()

#合并数据
all_data = jan_data+feb_data

#开始计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money


bar = Bar(init_opts=InitOpts(theme=ThemeType.ESSOS))
bar.add_xaxis(list(data_dict.keys()))  #x轴
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))  #y轴

#全局配置
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

#生成柱状图
bar.render("每日销售额柱状图.html")  #括号内名称

