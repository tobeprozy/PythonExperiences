from pyecharts.charts import Bar
# 新版要from pyecharts.charts import Bar
# 老版 from pyecharts import Bar
from pyecharts import options as opts

bar = Bar()
city = ["美国", "中国", "英国", "加拿大", "印度","以色列","法国","德国","瑞典","西班牙","日本","瑞士","荷兰","波兰","澳大利亚",
        "意大利","爱尔兰","韩国","新加坡","俄罗斯"]
data1 = [2028, 1011, 392, 282, 152,121,120,111,55,53,40,40,40,33,31,29,26,26,25,17]


bar = (
    Bar()
   .add_xaxis(city)
   .add_yaxis("国家", data1, stack="stack1")
   .reversal_axis()
   .set_series_opts(label_opts=opts.LabelOpts(position="right"),
                    markpoint_opts=opts.MarkPointOpts(
                    data=[
                     opts.MarkPointItem(type_="max", name="最大值"),
                     opts.MarkPointItem(type_="min", name="最小值"),
                         ]
                     )
                   )
   .set_global_opts(title_opts=opts.TitleOpts(title="人工智能分布"))
   .render('vzhuang.html')
)

