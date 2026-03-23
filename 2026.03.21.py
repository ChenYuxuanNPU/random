"""
用来可视化质量分析结果
"""

from pyecharts import options as opts
from pyecharts.charts import Bar

from func import *

data = read_xlsx_to_list(file_path="1.xlsx")


#
# temp = [int(item[0]) for item in data]
# print(Counter(temp))
# x_axis = [i for i in range(0, 100)]
# y_axis = []
# for item in x_axis:
#     y_axis.append(Counter(temp).get(item))

def extract_number_between(text, start_word="第", end_word="题"):
    """
    提取字符串中指定词语之间的数字

    Args:
        text: 输入字符串
        start_word: 起始词语
        end_word: 结束词语

    Returns:
        提取到的数字列表
    """
    pattern = rf'{start_word}(\d+){end_word}'
    matches = re.findall(pattern, text)
    return [int(num) for num in matches]


x_axis = []
y_axis = []
for item in data:
    x_axis.append(f"第{extract_number_between(item[0])[0]}题")
    y_axis.append(round(item[1] * 100, 2))

print(x_axis)
print(y_axis)

c = (
    Bar(
        init_opts=opts.InitOpts(
            width="100%",  # 设置宽度为100%，占满父容器
            height="800px"  # 高度可以固定像素，也可以设置为百分比
        )
    )
    .add_xaxis(x_axis)
    .add_yaxis(
        "八年级选择题",
        y_axis,
        label_opts=opts.LabelOpts(
            position="top",  # 设置标签位置在顶部
            font_size=30,  # 可选：设置字体大小
            color="black",  # 可选：设置字体颜色
            formatter="{c}%",  # 在数字后面添加百分号
            # is_show=False,
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="八年级",
        ),
        yaxis_opts=opts.AxisOpts(
            # interval=50,
            max_=100  # 动态设置最大值
        ),
        xaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(
                font_size=20  # 设置横坐标字体大小为14
            )
        ),
    )
    .render("bar_base.html")
)
