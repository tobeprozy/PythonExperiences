from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker


country=['China', 'Canada', 'United States', 'France', 'United Kingdom',
         'Netherlands', 'Germany', 'Australia', 'Japan',
         'Israel', 'Sweden']



num=[372,68,186,51,100,17,16,17,136,50,17]
print(Faker.country)
c = (
    Map()
    .add("", [list(z) for z in zip(country, num)], "world")

    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Major countries where AI companies are distributed",pos_left='30%'),
        visualmap_opts=opts.VisualMapOpts(max_=400,is_piecewise=True),

    )
    .render("map_world.html")
)