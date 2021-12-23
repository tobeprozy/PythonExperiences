from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

a1 = ["AI", "Intelligent Robot","Intelligent Driving","UAV ","Big Data","AR/VR"]
v1 = [46,22,5,6,17,3]

a11 =["AI", "Intelligent Robot","Intelligent Driving","UAV ","Big Data","AR/VR"]
v11 = [76,6,3,1,13,1]


from pyecharts import options as opts
from pyecharts.charts import Pie




print([list(z) for z in zip(a1, v1)])

c = (
    Pie()
    .add(
        "China",

        [list(z) for z in zip(a1, v1)],

        radius=["35%", "55%"],
        label_opts=opts.LabelOpts(
            position="inner",
            formatter="{d}%",)
    )


    .add(
        "Foreign",
        [list(z) for z in zip(a11, v11)],
        radius=["60%", "80%"],
        label_opts=opts.LabelOpts(
            position="inner",
            formatter="{d}%",)
    )


    .set_global_opts(
        title_opts=opts.TitleOpts(title="Domestic and foreign artificial intelligence enterprise industry distribution",
                                  pos_left="10%"),
        legend_opts=opts.LegendOpts(orient="scroll", pos_top="30%", pos_left="2%"),
        graphic_opts=[
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center",
                                top="middle",
                                z=100,
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                # 可以通过jsCode添加js代码，也可以直接用字符串
                                text="China",
                                font="14px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#333"
                                )
                            )
                        ),

            opts.GraphicText(
                graphic_item=opts.GraphicItem(
                    position=(200,230),
                    z=100,
                ),
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    text="Foreign",
                    font="14px Microsoft YaHei",
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill="#333"
                    )
                )
            )
                    ]
    )

    # .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    .render("Domestic and foreign artificial intelligence enterprise industry distribution.html")
)

