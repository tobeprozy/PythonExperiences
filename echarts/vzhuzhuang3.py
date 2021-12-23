from pyecharts.charts import Bar
# 新版要from pyecharts.charts import Bar
# 老版 from pyecharts import Bar
from pyecharts import options as opts

bar = Bar()
city = ["Beijing","Shanghai","Guangdong","Zhejiang","Jiangsu","Sichuan","Shanxi","Tianjin","Fujian","Hubei","Anhui","Shandong","Liaoning","Chongqing"]
data1 = [5.8,4.9,5.9,5.4,6.7,6.0,5.8,4.0,6.5,4.9,5.1,9.9,6.8,5.2]


bar = (
    Bar(init_opts=opts.InitOpts())
   .add_xaxis(city)
   .add_yaxis("City average", data1, stack="stack1")
   # .reversal_axis()
   .set_series_opts(label_opts=opts.LabelOpts(position="top"),
                    markpoint_opts=opts.MarkPointOpts(
                    data=[
                     opts.MarkPointItem(type_="max", name="max"),
                     opts.MarkPointItem(type_="min", name="min"),
                         ]
                     ),
                    markline_opts=opts.MarkLineOpts(
                        data=[
                            opts.MarkLineItem(type_="average", name="Average"),
                        ]
                   )
        )
   # .set_colors('red')
   .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
                    title_opts=opts.TitleOpts(title="Average age of ai companies in China's major provinces"
                                              ,pos_top='0%',pos_left="20%"),
                    legend_opts=opts.LegendOpts(pos_top='10%',pos_left="15%"))
   .render("Average age of ai companies in China's major provinces.html")
)

