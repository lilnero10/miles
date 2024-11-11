import webbrowser
import pandas as pd
from pyecharts.charts import *
from pyecharts import options as opts

def line_chart(t, data):
    # 新建一个折线图
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

def fl_chart(t, data):
    # 新建一个漏斗图
    chart = (
        Funnel(init_opts=opts.InitOpts(theme='light', width='600px', height='300px'))
        .add('', data, label_opts=opts.LabelOpts(formatter='{d}%', position='right'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title=t),
        legend_opts=opts.LegendOpts(pos_left="0%",pos_top="55",orient='vertical')
        )
    )
    return chart

if __name__ == '__main__':
    # 特征数据统计
    user_df = pd.read_csv('/Users/chenzhiyong/PycharmProjects/3_python算法练习/analyse_practice/douyin_data_analyse/用户数据可视化/用户特征.csv')
    user_df.head()

    # 不同浏览量用户占比
    bins = [0, 5, 10, 25, 50, 100, 1951]
    # 定义了一组区间，划分区间
    data = pd.cut(user_df['浏览量'], bins, right=True,
                  labels=[f'({bins[x]}，{bins[x+1]})' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()
    chart = pie_chart('不同浏览量用户占比', data)
    # # 指定 chromedriver 的路径
    # service = Service(
    #     '/usr/local/chromedriver-mac-arm64/chromedriver')
    # # 使用 Service 创建 Chrome WebDriver
    # driver = webdriver.Chrome(service=service)
    #
    # # 将图表保存为HTML并截图
    # chart_html = chart.render()  # 先将图表渲染为 HTML
    # img_path = "/Users/chenzhiyong/PycharmProjects/3_python算法练习/analyse_practice/douyin_data_analyse/用户数据可视化/用户特征.png"  # 选择一个临时路径保存图片
    # make_snapshot(snapshot, chart_html, img_path)
    #
    # # 读取并显示图片
    # img = Image.open(img_path)
    # plt.imshow(img)
    # plt.axis('off')  # 关闭坐标轴
    # plt.show()

    # 保存图片为HTML格式
    chart_path_html = '/Users/chenzhiyong/PycharmProjects/3_python算法练习/analyse_practice/douyin_data_analyse/用户数据可视化/不同浏览量用户占比.html'
    chart.render(chart_path_html)
    webbrowser.open(chart_path_html)

    # 用户完整观看情况
    bins = [0, 5, 10, 20, 30, 50, 284]
    data = pd.cut(user_df['完整观看数'], bins, right=True,
                  labels=[f'({bins[x]}，{bins[x+1]})' for x in range(len(bins)-1)]).value_counts().reset_index().values.tolist()
    pie_chart('完整观看情况', data).render_notebook()

    # 去过不同数量城市的用户占比
    data = user_df['去过的城市数'].value_counts().reset_index().values.tolist()
    pie_chart('去过不同数量城市的用户占比', data).render_notebook()

    # 不同点赞量用户占比
    bins = [-1, 0, 1, 183]
    data = pd.cut(user_df['点赞量'], bins, right=True,
                  labels=[f'({bins[x]}，{bins[x+1]})' for x in range(len(bins)-1)]).value_counts().reset_index().sort_values(by='index').values.tolist()
    pie_chart('不同点赞量用户占比', data).render_notebook()

    # 用户点赞量
    temp = user_df['点赞量'].sort_values(ascending=False).reset_index().cumsum()['点赞量']
    temp = temp/temp.max()
    data = temp.reset_index().values.tolist()
    line_chart('用户点赞量', data).render_notebook()

    # 用户累计浏览量占比
    temp = user_df['浏览量'].sort_values(ascending=False).reset_index().cumsum()['浏览量']
    temp = temp/temp.max()
    data = temp.reset_index().values.tolist()
    line_chart('用户累计浏览量占比', data).render_notebook()

    # 观看作品平均时长
    bins = [1, 10, 12, 15, 42]
    data = pd.cut(
        user_df['观看作品平均时长'],
        bins, right=True,labels=[f'({bins[x]}, {bins[x+1]}]' for x in range(len(bins)-1)]
    ).value_counts()
    data = data.sort_index(ascending=False).cumsum().reset_index().values.tolist()
    fl_chart('观看作品平均时长', data).render_notebook()

    _ = temp.tolist()
    for j in range(10):
        j /= 10
        for i in _:
            if i >= j:
                flag = i
                break
        c = _.index(flag)/len(_)
        print(f'{c:4.1%} 的用户点了{j:3.0%} 的赞')