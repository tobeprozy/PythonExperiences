from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line



city = ["2015", "2016", "2017", "2018","2010", "2020"]
data1 = [160,170,210,405,700,980]


bar = (
    Bar()
   .add_xaxis(city)
   .add_yaxis("Market Scale", data1, stack="stack1",z=1)

   # .reversal_axis()
   .set_series_opts(label_opts=opts.LabelOpts(position="top"),
                    markpoint_opts=opts.MarkPointOpts(
                    data=[
                     # opts.MarkPointItem(type_="max", name="最大值"),
                     # opts.MarkPointItem(type_="min", name="最小值"),
                         ]
                     )
                   )

    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="Percentage",
            min_=0,
            max_=80,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}%"),

        )
    )

        .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="Dollar(/Trillion)",
            min_=0,
            max_=1200,
            position="left",
            offset=0,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        ),

        title_opts=opts.TitleOpts(title="The scale of China's Artificial intelligence market from 2015 to 2020",
                                  pos_bottom='0%',pos_left='7%'),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)


city1 = ["2015","2016", "2017", "2018","2010", "2020"]
data11 = [100,400,1000,1130,1000,595]

line = (
    Line()

    .add_xaxis(city1)
    .add_yaxis("Growth rate", data11,label_opts=opts.LabelOpts(is_show=False),z=10,color='black')


)



bar.overlap(line)

grid = Grid()
grid.add(bar, opts.GridOpts(pos_top="10%",pos_left="5%", pos_right="20%"), is_control_axis_index=True)
# grid.add(line, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid.render("The scale of China's Artificial intelligence market from 2015 to 2020.html")