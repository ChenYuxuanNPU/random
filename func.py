import sqlite3

import openpyxl


def del_tuple_in_list(data: list) -> list:
    """
    将形如[('1',), ('2',), ('3',),]的数据转化为[1, 2, 3,]
    :param data:带有元组的列表
    :return: 清洗后的列表
    """

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


def read_xlsx_to_list(file_path, sheet_name=None):
    # 打开工作簿
    workbook = openpyxl.load_workbook(file_path)

    # 如果未指定工作表名称，则使用第一个工作表
    if sheet_name is None:
        sheet = workbook.active
    else:
        sheet = workbook[sheet_name]

    # 读取数据并存储到二维列表中
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    return data


def save_excel(two_dimension_list: list[list or tuple], excel_name: str = "output"):
    # 读取 Excel 文件
    workbook = openpyxl.Workbook()

    # 获取活动的工作表
    ws = workbook.active

    for item in two_dimension_list:
        ws.append(item)

    workbook.save(f"{excel_name}.xlsx")
