import pandas as pd
from pyecharts import Geo

# 读取数据
datafile = ('tavel.xlsx')
data = pd.read_excel(datafile)
attr = data['City']
value = data['Score']

geo = Geo("♡♡♡  往后余生，踏遍山河  ♡♡♡", title_color="#2E2E2E",
          title_text_size=24, title_top=20, title_pos="center", width=1300, height=600,
          background_color='#F6CEF5')
geo.add("", attr, value, type="effectScatter", is_random=True, visual_range=[0, 100],
        maptype='china', visual_text_color="#FF0000", geo_normal_color="#6E6E6E", geo_emphasis_color='#F5D0A9',
        symbol_size=8, effect_scale=5, is_visualmap=True)

geo.render('往后余生.html')  # 生成html文件