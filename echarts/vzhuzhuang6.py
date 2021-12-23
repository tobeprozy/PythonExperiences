from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line



city = ["2013", "2014", "2015", "2016", "2017", "2018"]
data1 = [18,48,145,210,275,74]

data2 = [49,130,280,315,395,100]

bar = (
    Bar()
   .add_xaxis(city)
   .add_yaxis("China", data1, stack="stack1",z=1)
   .add_yaxis("Global", data2, stack="stack2",z=1)
   # .reversal_axis()
   .set_series_opts(label_opts=opts.LabelOpts(position="top"),
                    markpoint_opts=opts.MarkPointOpts(
                    data=[
                     opts.MarkPointItem(type_="max", name="max"),
                     opts.MarkPointItem(type_="min", name="min"),
                         ]
                     )
                   )

    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="Count",
            min_=0,
            max_=1400,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),

        )
    )

        .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="Money",
            min_=0,
            max_=450,
            position="left",
            offset=0,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="black")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        ),

        title_opts=opts.TitleOpts(title="Global AI investment and financing trends",pos_bottom="0%",pos_left="20%"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)



data11 = [18,48,80,105,118,20]
data22 = [100,155,220,295,395,58]
line = (
    Line()
    .add_xaxis(city)
    .add_yaxis("China", data11,label_opts=opts.LabelOpts(is_show=False),z=10,color='black')
    .add_yaxis("Global", data22,label_opts=opts.LabelOpts(is_show=False),z=10,color='blue')

)



bar.overlap(line)

grid = Grid()
grid.add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid.add(line, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid.render("Global AI investment and financing trends.html")