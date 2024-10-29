import sqlite3
import json
from pathlib import Path
from typing import Tuple
import openpyxl


def get_database_name() -> str:
    """
    根据database_basic_info.json获取数据库名
    :return: 数据库名
    """

    with open(fr"{Path(__file__).resolve().parent.parent.parent}\json_file\database\database_basic_info.json",
              "r", encoding='UTF-8') as file:  # ISO-8859-1
        loaded_data = json.load(file)

    database_name = loaded_data["database_name"]

    return database_name


# kind:"在编","编外"
def connect_database() -> Tuple[sqlite3.Cursor, sqlite3.Connection]:
    """
    用于连接数据库
    :return:
    """

    conn = sqlite3.connect(
        fr"C:\Users\1012986131\Desktop\python\random\30\educational_data.db"
    )
    c = conn.cursor()

    return c, conn


def disconnect_database(conn) -> None:
    """
    用于断开数据库
    :param conn:
    :return:
    """

    conn.close()

    return None


def execute_sql_sentence(sentence: str,) -> list:
    """
    执行数据库语句并返回列表
    :param sentence: 需要执行的语句
    :return:
    """

    c, conn = connect_database()

    result = []
    try:
        c.execute(sentence)
        result = c.fetchall()

    except Exception as e:
        print(e)

    disconnect_database(conn=conn)

    return result


def del_tuple_in_list(data: list) -> list:
    """
    将形如[('1',), ('2',), ('3',),]的数据转化为[1, 2, 3,]
    :param data:带有元组的列表
    :return: 清洗后的列表
    """

    if not isinstance(data[0], tuple):
        return data

    output = []

    for single_data in data:
        output.append(single_data[0])

    return output


school_list = del_tuple_in_list(execute_sql_sentence(sentence='select distinct "校名" from teacher_data_0_2024 where "学校类型" != "教学支撑单位"'))

output = []
exclude_list = []

for school in school_list:

    result = list(execute_sql_sentence(f'select "统一社会信用代码", "校名", "学校类型", count(*) from teacher_data_0_2024 where "校名" == "{school}" and ("任教学段" = "小学" or "任教学段" == "初中")')[0])

    if result[0] == None:
        exclude_list.append(school)
        continue

    raw_data = execute_sql_sentence(f'select "交流结束时间" from teacher_data_0_2024 where "校名" == "{school}" and ("任教学段" = "小学" or "任教学段" == "初中")')

    count = 0

    for item in raw_data:
        if item[0] == "无":
            count += 1

        elif item[0][:4].isdigit():
            if int(item[0][:4]) < 2015:
                count += 1

        else:
            print("???")

    result.append(count)

    output.append(result)


print(output)

print(len(output))
print(len(exclude_list))
print(exclude_list)

# 创建一个新的工作簿
wb = openpyxl.Workbook()

# 选择活动的工作表
ws = wb.active

# 给工作表命名（可选）
ws.title = "Sheet1"

# 将二维列表的每一行写入工作表
for row in output:
    ws.append(row)

ws2 = wb.create_sheet(title="Sheet2")
for row in exclude_list:
    ws2.append([row])

# 保存工作簿到文件
wb.save("output.xlsx")


