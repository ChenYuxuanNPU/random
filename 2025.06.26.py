"""
用于生成全区期末考试的成绩柱状图
"""

from collections import Counter

import pandas as pd
import pyecharts.options as opts
import streamlit as st
from pyecharts.charts import Bar, Line
from pyecharts.options import InitOpts
from streamlit_echarts import st_pyecharts

from func import *

st.set_page_config(
    layout='wide'
)


grade = "八年级"

data = read_xlsx_to_list(
    file_path=r"C:\Users\1012986131\Desktop\2024学年下学期期末诊断调研质量分析\信息科技考试数据源.xlsx",
    sheet_name=grade)[1:]

grade_list = [int(item[-4]) for item in data][::-1]
grade_dict = dict(Counter(grade_list))

st_pyecharts(
    Bar()
    .add_xaxis(list(grade_dict.keys()))
    .add_yaxis("成绩", list(grade_dict.values()))
    .set_global_opts(title_opts=opts.TitleOpts(title=grade))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False)),
    height="750px",
    width="1920px"
)
