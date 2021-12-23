from pyecharts.charts import Bar
# 新版要from pyecharts.charts import Bar
# 老版 from pyecharts import Bar
from pyecharts import options as opts

bar = Bar()
city = ["Beijing ", "San Francisco" ,"London", "Shanghai", "New York", "Shenzhen", "Boston", "Toronto", "Paloalto", "Paris", "Telaviv", "Hangzhou", "Montreal", "Vancouver", "Mountain",
"Berlin","SAN Jose","Sunnyvale","Austin","Seattle"]
data1 = [395,287,274,210,188,119,117,109,105,83,64,63,58,56,51,48,46,46,45,38]


bar = (
    Bar()

   .add_xaxis(city)
   .add_yaxis("City", data1, stack="stack1")
   .reversal_axis()
   .set_series_opts(label_opts=opts.LabelOpts(position="right"),
                    markpoint_opts=opts.MarkPointOpts(
                    data=[
                     opts.MarkPointItem(type_="max", name="max"),
                     opts.MarkPointItem(type_="min", name="min"),                         ]
                     )
                   )
   .set_global_opts(title_opts=opts.TitleOpts(title="The number of artificial intelligence enterprises in the world TOP 20 cities",pos_left="10%"),
                    legend_opts=opts.LegendOpts(pos_top='10%'))
   .render('The number of artificial intelligence enterprises in the world TOP 20 cities.html')
)

