from pyecharts import Bar
import os
import pandas as pd

os.chdir("D:/python/project/first/echarts")
data=pd.read_excel('房价与工资.xlsx',header=None)
print(data)
x=data[0][1:]
y1=data[2][1:]
y2=data[3][1:]
print(x,y1,y2)
bar = Bar()
bar.add("房价均价",x,y1,mark_point=["max","min"],mark_line=["average"],is_label_show=True)
bar.add("人均工资",x,y2,xaxis_rotate=30,yaxis_rotate=30)
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()