# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_csv('movies.csv',encoding='gbk')
# df.describe()
#评分大于8分的电影
rate_score = df.loc[df.rate >= 8]
# print(rate_score)

# 按评分排名
rating = df.sort_values(by='rate',ascending=False)
print(rating.head(10))

# 什么类型的电影最多
genres = list((df['genres'].dropna().values))
all = []
for each in genres:
    all.extend(each.split('/'))
print(Counter(all).most_common(10))

# 合作过的演员
casts = list((df['casts'].dropna().values))
all = []
for each in casts:
    all.extend(each.split('/'))
print(Counter(all).most_common(10))
# 合作过的导演
directors = list((df['directors'].dropna().values))
all = []
for each in directors:
    all.extend(each.split('/'))
print(Counter(all).most_common(10))


year = df['year']
plt.scatter(x,y,data=year)
plt.xlabel('year')
plt.ylabel('movies')
plt.show()





