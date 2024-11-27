import sqlite3
import copy
import openpyxl
from openpyxl import Workbook


def del_tuple_in_list(data: list) -> list:
    """
    将形如[('1',), ('2',), ('3',),]的数据转化为[1, 2, 3,]
    :param data:带有元组的列表
    :return: 清洗后的列表
    """

    if not isinstance(data[0], tuple):
        return data

    output = []

    output.extend(single_data[0] for single_data in data)

    return output


def execute_sql_sentence(sentence: str, ) -> list:
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


# kind:"在编","编外"
def connect_database() -> tuple[sqlite3.Cursor, sqlite3.Connection]:
    """
    用于连接数据库
    :return:
    """

    conn = sqlite3.connect(
        fr"C:\Users\1012986131\Desktop\python\streamlit_pyecharts\database\educational_data.db"
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


if __name__ == '__main__':
    result = execute_sql_sentence(
        sentence=f'select "姓名", "现聘职称", "主教学科", "区域", "校名", "任教学段" from teacher_data_0_2024 where "现聘职称" not like "%非中小学系列%" and "任教学段" != "其他" and "任教学段" != "中职" and "主教学科" != "无"')
    school_list = del_tuple_in_list(
        execute_sql_sentence(sentence='select distinct "校名" from teacher_data_0_2024 where "区域" = "直管"'))
    discipline_list = del_tuple_in_list(
        execute_sql_sentence(sentence='select distinct "主教学科" from teacher_data_0_2024'))

    print(del_tuple_in_list(execute_sql_sentence(
        sentence='select distinct "现聘职称" from teacher_data_0_2024 where "现聘职称" not like "%非中小学系列%"')))

    convert_dict = {
        "高级教师": "高级教师",
        "试用期未聘": "初级教师",
        "二级教师": "初级教师",
        "一级教师": "中级教师",
        "未取得职称": "初级教师",
        "三级教师": "初级教师",
        "正高级教师": "高级教师"
    }

    period_list = ["高中", "初中", "小学", "幼儿园"]
    dict1 = {}
    dict1_3 = {
        "高级教师": 0,
        "中级教师": 0,
        "初级教师": 0
    }
    dict1_2 = {key: copy.deepcopy(dict1_3) for key in period_list}
    dict1_1 = {key: copy.deepcopy(dict1_2) for key in discipline_list}

    for keyss in ["永平", "石井", "新市", "江高", "人和", "太和", "钟落潭"]:
        dict1[keyss] = copy.deepcopy(dict1_1)

    for keyss in school_list:
        dict1[keyss] = copy.deepcopy(dict1_1)

    dict_output = copy.deepcopy(dict1)
    test = []
    count0 = 0
    count1 = 0
    for item in result:
        if item[3] == "直管":
            count0 += 1
            dict_output[item[4]][item[2]][item[5]][convert_dict[item[1]]] += 1
        else:
            count1 += 1
            dict_output[item[3]][item[2]][item[5]][convert_dict[item[1]]] += 1
            if item[3] == "永平" and item[2] == "语文" and item[5] == "小学":
                test.append(item)


    print(dict_output)

    # print(execute_sql_sentence(sentence=f'select "现聘职称",count(*)  from teacher_data_0_2024 where "区域" = "永平" and "现聘职称" not like "%非中小学系列%" and "任教学段" = "小学"  and "主教学科" == "语文" group by "现聘职称"'))

    for area, value in dict_output.items():

        wb = Workbook()

        wb.remove(wb.active)

        ws = wb.create_sheet(title="数据")

        for discipline in discipline_list:

            data = value[discipline]

            temp = []

            for key in data.keys():
                for key1,value1 in data[key].items():
                    temp.append([discipline,key,key1,value1])

                temp.append([discipline,key,"中高级教师占比", (temp[-2][3] + temp[-3][3]) / (temp[-1][3] + temp[-2][3] + temp[-3][3]) if (temp[-1][3] + temp[-2][3] + temp[-3][3]) != 0 else 0])
            for item in temp:
                ws.append(item)
        wb.save(fr'C:\Users\1012986131\Desktop\python\random\output\{area}.xlsx')






