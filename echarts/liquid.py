# -*- coding:utf-8 -*-
from pyecharts import Liquid

liquid = Liquid("水球图")
liquid.add("Liquid", [0.8])
liquid.show_config()
liquid.render('Liquid.html')