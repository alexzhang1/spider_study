# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
# %matplotlib inline
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('lianjia_demo.csv', encoding='utf-8')
del df['href']
df.info()
mean_price_per_region = df.groupby(df.region)

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)

ax.set_title(u'南京各区域二手房平均价格')
mean_price_per_region.unit_price.mean().plot.bar()
plt.savefig('mean_price.jpg')
plt.show()