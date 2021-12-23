from pyecharts import options as opts
from pyecharts.charts import Pie




attr =[" Chinese ", "Singapore", "South Korea", "Japan", "Spanish", "Germany", "Israel", "French", "India", "Canada", "Britain" , "American"]
v1 =[22,1,1,1,1,1,3,3,3,4,8,11,41]


c = (
    Pie()
    .add("", [list(z) for z in zip(attr, v1)],
         label_opts=opts.LabelOpts(
             position="outsize",
             formatter="{d}%", )
         )
    # .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="AI enterprises around the world",pos_left='30%'),
                     legend_opts=opts.LegendOpts(
                         type_="scroll", pos_top="10%", pos_left="80%", orient="vertical")
                     )

    .render("AI enterprises around the world.html")
)

