import pandas as pd
import numpy as np

from pyecharts.charts import *
from pyecharts import options as opts

def line_chart(t, data):
    chart = (
        Line(init_opts = opts.InitOpts(theme='light', width='500px', height='300px'))
        .add_xaxis([i[0] for i in data])
        .add_yaxis(
            '',
            [i[1] for i in data],
            is_symbol_show=False,
            areastyle_opts=opts.AreaStyleOpts(opacity=1, color="cyan")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=t),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
    )
    return chart

def pie_chart(t, data_pair):
    # 新建一个饼图
    chart = (
        Pie(init_opts=opts.InitOpts(theme='light', width='550px', height='300px'))
        .add('', data_pair ,radius=["30%", "45%"], # 半径范围，内径和外径
            label_opts=opts.LabelOpts(formatter="{b}: {d}%") # 标签设置，{d}表示显示百分比
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=t
             ),
            legend_opts=opts.LegendOpts(pos_left="0%",pos_top="55",orient='vertical')
        )
    )
    return chart

# 数据指标统计
author_df = pd.read_csv('')
author_df.head()

# 不同浏览量作者占比
bins = [0, 1, 5, 10, 20, 50, 2648]
data = pd.cut(author_df['总浏览量'], bins, right=True,labels=[f'({bins[x]}，{bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()
pie_chart('不同浏览量作者占比', data).render_notebook()

# 作者累计浏览量占比
temp = author_df['总浏览量'].sort_values(ascending=False).reset_index().cumsum()['总浏览量'].reset_index()
temp = temp/temp.max()
temp['index'] = temp['index'].apply(lambda x: format(x, '.2%'))
data = temp[temp['总浏览量']<0.90].values.tolist()

line_chart('作者累计浏览量占比', data).render_notebook()

#不同点赞量作者占比
bins = [-1, 0, 1, 36]
data = pd.cut(author_df['总点赞量'], bins, right=True,labels=[f'({bins[x]}，{bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().sort_values(by='index').values.tolist()
pie_chart('不同点赞量作者占比', data).render_notebook()

# 作者累计点赞量
temp = author_df['总点赞量'].sort_values(ascending=False).reset_index().cumsum()['总点赞量'].reset_index()
temp = temp/temp.max()
temp['index'] = temp['index'].apply(lambda x: format(x, '.2%'))
data = temp[temp['总点赞量']<0.999999999999999999].values.tolist()

line_chart('作者累计点赞量', data).render_notebook()

_ = temp['总点赞量'].tolist()
for j in range(10):
    j /= 10
    for i in _:
        if i>=j:
            flag = i
            break
    c = _.index(flag)/len(_)
    print(f'{c:4.1%} 的作者获得了{j:3.0%} 的赞')

#作者去过的城市数量分布
bins = [0, 1, 2, 10, 19]
data = pd.cut(author_df['去过的城市数'], bins, right=True,labels=[f'({bins[x]}，{bins[x+1]}]' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()
pie_chart('作者去过的城市数量分布', data).render_notebook()