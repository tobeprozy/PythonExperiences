# -*- coding:utf-8 -*-
from pyecharts import Gauge

g = Gauge("仪表盘图形", "副图标")
g.add("重大项目", "投资占比", 66.66)
g.show_config()
g.render("g.html")