from pyecharts import Pie
import os
import pandas as pd

os.chdir("D:/python/project/first/echarts")
data=pd.read_excel('房价与工资.xlsx',header=None)
print(data)
x=data[1][1:]
y1=data[2][1:]
y2=data[3][1:]
print(x,y1,y2)

pie = Pie()
# pie.add('房屋均价',x,y1,mark_point=["max","min"],mark_line=["average"],is_label_show=True,legend_orient='vertical', legend_pos='right')
pie.add('人均工资', x, y2, is_label_show=True, legend_pos='left')
pie.render('饼状图01.html')