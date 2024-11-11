import pandas as pd
import numpy as np

df = pd.read_csv('/Users/chenzhiyong/Downloads/python_analyse/douyin_dataset.csv')
df.head()

# Drop the first column
df = df.iloc[:, 1:]

# 数据基本信息基本信息
df.info()

# 用户特征统计分析
user_df = pd.DataFrame()
user_df['uid'] = df.groupby('uid')['like'].count().index.tolist() # 将所有用户的uid提取为uid列
user_df.set_index('uid', inplace=True) # 设置uid列为index，方便后续数据自动对齐
user_df['浏览量'] = df.groupby('uid')['like'].count() # 统计对应uid下的浏览量
user_df['点赞量']  = df.groupby('uid')['like'].sum() # 统计对应uid下的点赞量
user_df['观看作者数'] = df.groupby(['uid']).agg({'author_id':pd.Series.nunique}) # 观看作者数
user_df['观看作品数'] = df.groupby(['uid']).agg({'item_id':pd.Series.nunique}) # 观看作品数
user_df['观看作品平均时长'] = df.groupby(['uid'])['duration_time'].mean() # 浏览作品平均时长
user_df['观看配乐数'] = df.groupby(['uid']).agg({'music_id':pd.Series.nunique}) # 观看作品中配乐的数量
user_df['完整观看数']  = df.groupby('uid')['finish'].sum() # 统计对应uid下的完整观看数
# 统计对应uid用户去过的城市数量
user_df['去过的城市数'] = df.groupby(['uid']).agg({'user_city':pd.Series.nunique})
# 统计对应uid用户看的作品所在的城市数量
user_df['观看作品城市数'] = df.groupby(['uid']).agg({'item_city':pd.Series.nunique})
user_df.describe()

user_df.to_csv('用户特征.csv', encoding='utf_8_sig')

# 作者特征统计分析
author_df = pd.DataFrame()
author_df['author_id'] = df.groupby('author_id')['like'].count().index.tolist()
author_df.set_index('author_id', inplace=True)
author_df['总浏览量'] = df.groupby('author_id')['like'].count()
author_df['总点赞量']  = df.groupby('author_id')['like'].sum()
author_df['总观完量']  = df.groupby('author_id')['finish'].sum()
author_df['总作品数'] = df.groupby('author_id').agg({'item_id':pd.Series.nunique})

item_time = df.groupby(['author_id', 'item_id']).mean().reset_index()
author_df['作品平均时长'] = item_time.groupby('author_id')['duration_time'].mean()

author_df['使用配乐数量'] = df.groupby('author_id').agg({'music_id':pd.Series.nunique})
author_df['发布作品日数'] = df.groupby('author_id').agg({'real_time':pd.Series.nunique})

# pd.to_datetime(df['date'].max()) - pd.to_datetime(df['date'].min()) # 作品时间跨度为40，共计40天
author_days = df.groupby('author_id')['date']
_ = pd.to_datetime(author_days.max()) - pd.to_datetime(author_days.min())
author_df['创作活跃度(日)'] = _.astype('timedelta64[D]').astype(int) + 1
author_df['去过的城市数'] = df.groupby(['author_id']).agg({'item_city':pd.Series.nunique})
author_df.describe()

author_df.to_csv('作者特征.csv', encoding='utf_8_sig')

# 作品特征统计分析
item_df = pd.DataFrame()
item_df['item_id'] = df.groupby('item_id')['like'].count().index.tolist()
item_df.set_index('item_id', inplace=True)
item_df['浏览量'] = df.groupby('item_id')['like'].count()
item_df['点赞量']  = df.groupby('item_id')['like'].sum()
item_df['发布城市'] = df.groupby('item_id')['item_city'].mean()
item_df['背景音乐'] = df.groupby('item_id')['music_id'].mean()

item_df.to_csv('作品特征.csv', encoding='utf_8_sig')