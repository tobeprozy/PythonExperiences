from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

a1 = ["Natural Language Processing","Speech","Vision","Basic Hardware"]
v1 = [19, 22,46,14]

a11 = ["Natural Language Processing","Speech","Vision","Basic Hardware"]
v11 = [28, 22,40,20]


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
        title_opts=opts.TitleOpts(title="Artificial intelligence enterprise application technology distribution at home and abroad"),
        legend_opts=opts.LegendOpts(orient="scroll", pos_top="40%", pos_left="2%"),
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
                    # 可以通过jsCode添加js代码，也可以直接用字符串
                    text="foreign",
                    font="14px Microsoft YaHei",
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill="#333"
                    )
                )
            )
                    ]
    )

    # .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

    .render("Artificial intelligence enterprise application technology distribution at home and abroad.html")
)

