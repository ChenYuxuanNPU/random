"""
统计不同类型单位的第一学历985、211、前十五师范院校和最高学历985、211、前十五师范院校人数和占比
"""
import json

with open(fr"C:\Users\1012986131\Desktop\python\streamlit_pyecharts\json_file\source\院校代码.json",
          "r", encoding="UTF-8") as f:
    search_school_id = json.load(f)

with open(fr"C:\Users\1012986131\Desktop\python\streamlit_pyecharts\json_file\source\院校级别.json",
          "r", encoding="UTF-8") as f:
    id_list_for_9895211 = json.load(f)

top_15_normal = "北京师范大学 东北师范大学 华东师范大学 南京师范大学 华中师范大学 湖南师范大学 华南师范大学 陕西师范大学 西北师范大学 海南师范大学 内蒙古师范大学 云南师范大学 四川师范大学 曲靖师范学院 西南大学".split()
name_list_985 = "北京大学 中国人民大学 清华大学 北京航空航天大学 北京理工大学 中国农业大学 北京师范大学 中央民族大学 南开大学 天津大学 大连理工大学 东北大学 吉林大学 哈尔滨工业大学 复旦大学 同济大学 上海交通大学 华东师范大学 南京大学 东南大学 浙江大学 中国科学技术大学 厦门大学 山东大学 中国海洋大学 武汉大学 华中科技大学 湖南大学 中南大学 国防科学技术大学 中山大学 华南理工大学 四川大学 电子科技大学 重庆大学 西安交通大学 西北工业大学 西北农林科技大学 兰州大学 北京协和医学部 东北大学（秦皇岛） 哈尔滨工业大学（威海） 山东大学（威海）".split()
name_list_211 = "北京大学 中国人民大学 清华大学 北京交通大学 北京工业大学 北京航空航天大学 北京理工大学 北京科技大学 北京化工大学 北京邮电大学 中国农业大学 北京林业大学 北京中医药大学 北京师范大学 北京外国语大学 中国传媒大学 中央财经大学 对外经济贸易大学 北京体育大学 中央音乐学院 中央民族大学 中国政法大学 华北电力大学 南开大学 天津大学 天津医科大学 河北工业大学 太原理工大学 内蒙古大学 辽宁大学 大连理工大学 东北大学 大连海事大学 吉林大学 延边大学 东北师范大学 哈尔滨工业大学 哈尔滨工程大学 东北农业大学 东北林业大学 复旦大学 同济大学 上海交通大学 华东理工大学 东华大学 华东师范大学 上海外国语大学 上海财经大学 上海大学 第二军医大学 南京大学 苏州大学 东南大学 南京航空航天大学 南京理工大学 中国矿业大学 河海大学 江南大学 南京农业大学 中国药科大学 南京师范大学 浙江大学 安徽大学 中国科学技术大学 合肥工业大学 厦门大学 福州大学 南昌大学 山东大学 中国海洋大学 郑州大学 武汉大学 华中科技大学 武汉理工大学 华中农业大学 华中师范大学 中南财经政法大学 湖南大学 中南大学 湖南师范大学 国防科学技术大学 中山大学 暨南大学 华南理工大学 华南师范大学 海南大学 广西大学 四川大学 西南交通大学 电子科技大学 四川农业大学 西南财经大学 西南大学 重庆大学 贵州大学 云南大学 西藏大学 西北大学 西安交通大学 西北工业大学 西安电子科技大学 长安大学 西北农林科技大学 陕西师范大学 第四军医大学 兰州大学 青海大学 宁夏大学 新疆大学 石河子大学 北京协和医学部 华北电力大学（保定） 中国石油大学（华东） 中国地质大学（北京） 中国矿业大学（北京） 中国石油大学（北京） 中国地质大学（武汉） 东北大学（秦皇岛） 哈尔滨工业大学（威海） 山东大学（威海）".split()
top_15_normal_id = []

for school in top_15_normal:
    for id in search_school_id.keys():
        if search_school_id[id][0] == school:
            top_15_normal_id.append(id)

print()

