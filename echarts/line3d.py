from pyecharts import Line3D
import random
data = [[1,2,3,4], [1,2,3,4], [0,4,8,16]]
Line3D = Line3D("3D 折线图示例", width=1200, height=600)
Line3D.add("", data, is_visualmap=True)
Line3D.render('Line3D.html')