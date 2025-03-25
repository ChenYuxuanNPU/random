from random import shuffle

import openpyxl


def save_excel(two_dimension_list: list[list or tuple], excel_name: str = "output"):
    workbook = openpyxl.Workbook()

    ws = workbook.active

    for item in two_dimension_list:
        ws.append(item)

    workbook.save(f"{excel_name}.xlsx")


name_list = "张剑威 邵芳芳 刘蓉 欧阳嘉欣 陈燕贤 陈康 王志平 黄玉瑜 林佳婷 徐国平 曾祥力 钟慧珍 蔡子锋 邱洁晓 陈立华 廖诗剑 吕芳 叶丽芳 毕志鹏 李妙贞 陈歆怡 伍婉秋 康冬丽 宋艳梅 刘丽霞 郑泽吟".split()

shuffle(name_list)

list_2 = name_list[:int(len(name_list) / 3) + 1]
list_3 = name_list[int(len(name_list) / 3) + 1:int(len(name_list) / 3) * 2 + 2]
list_4 = name_list[int(len(name_list) / 3) * 2 + 2:]

output = [["第二单元", "第三单元", "第四单元"]]

for i in range(max(len(list_2), len(list_3), len(list_4))):
    output.append([
        list_2[i] if i < len(list_2) else None,
        list_3[i] if i < len(list_3) else None,
        list_4[i] if i < len(list_4) else None,
    ])

# save_excel(two_dimension_list=output, excel_name="命题范围安排")

for i in range(3):
    print(f"{output[0][i]}：{str([item[i] for item in output if item[i] is not None][1:])[1:-1]}")
