
from pyecharts import Bar


attr = ['{}月'.format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.8, 48.7, 18.8, 6.0, 2.3]
bar = Bar("柱状图示例")
bar.add("蒸发量", attr, v1, mark_line=['average'], mark_point=["max", "min"])  # 画平均线，标记最大最小值
bar.add("降水量", attr, v2, mark_line=['average'], mark_point=["max", "min"])
bar.render()

bar = Bar("x 轴和 y 轴交换")  # print交换x轴和y轴
bar.add("蒸发量", attr, v1, mark_line=['average'], mark_point=["max", "min"])
bar.add("降水量", attr, v2, mark_line=['average'], mark_point=["max", "min"], is_convert=True)  # is_convert是否转换
bar.render('降水量柱状图.html')