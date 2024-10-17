from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

list2 = [
    {"value": 10, "percent": 10 / (10 + 5)},
    {"value": 20, "percent": 20 / (20 + 15)},
    # ...继续添加数据
]

list3 = [
    {"value": 5, "percent": 5 / (10 + 5)},
    {"value": 15, "percent": 15 / (20 + 15)},
    # ...继续添加数据
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(["Category A", "Category B", "Category C", "Category D", "Category E"])
    .add_yaxis("Custom Product 1", list2, stack="stack1", category_gap="40%", color="blue")
    .add_yaxis("Custom Product 2", list3, stack="stack1", category_gap="40%", color="green")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return 'Ratio: ' + Number(x.data.percent * 100).toFixed(2) + '%';}"
            ),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="sakuraaasd_test", subtitle="Example Subtitle"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
    )
    .render("custom_stack_bar_percent.html")
)

