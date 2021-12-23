from pyecharts import options as opts
from pyecharts.charts import Pie




attr =[" Algorithms ", "Hardware "," Speech ", "Vision "," Natural Language Processing "]
v1 =[8,11.3,24.8,34.9,21]


c = (
    Pie()
    .add("", [list(z) for z in zip(attr, v1)],
         label_opts=opts.LabelOpts(
             position="outsize",
             formatter="{d}%",
         )
         )

    # .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_global_opts(title_opts=opts.TitleOpts(title="China's AI market structure", pos_left='35%'),
                 legend_opts=opts.LegendOpts(
                     type_="scroll", pos_bottom="0%", pos_left="20%")
                 )

    .render("China's AI market structure.html")
)



