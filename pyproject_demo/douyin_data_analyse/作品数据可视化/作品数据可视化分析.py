import pandas as pd
import numpy as np

from pyecharts.charts import *
from pyecharts import options as opts

def line_chart(t, data):
    #新建折线图
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

if __name__ == '__main__':
    #数据读取
    df =  pd.read_csv('')#数据绝对路径
    del df['Unnamed: 0']
    item_df = pd.read_csv('作品特征.csv')
    item_df.head()

    # 统计各日发布的作品数
    data = df.groupby(['date']).agg({'item_id':pd.Series.nunique}).reset_index().values.tolist()
    line_chart("各日单日作品发布量", data).render_notebook()

    #作品浏览量分布
    bins = [0, 1, 2, 4, 1600]
    item_df['浏览量等级'] = pd.cut(item_df['浏览量'], bins, labels=[f'({bins[x]}，{bins[x+1]}]' for x in range(len(bins)-1)])
    data = item_df.groupby('浏览量等级')['浏览量'].count().reset_index().values.tolist()
    pie_chart('作品浏览量分布', data).render_notebook()

    # 点赞数分布
    bins = [-1, 0, 1, 3, 5, 10, 35]
    item_df['点赞等级'] = pd.cut(item_df['点赞量'], bins, labels=[f'[{bins[x]}，{bins[x+1]})' for x in range(len(bins)-1)], right=False)
    data = item_df.groupby('点赞等级')['点赞量'].sum().reset_index().values.tolist()
    pie_chart('点赞数分布', data).render_notebook()