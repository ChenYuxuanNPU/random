import sqlite3

from func import *


def list_to_sqlite_db(data_list, db_file, table_name="data_table"):
    """
    将二维字符串列表转换为SQLite数据库文件
    :param data_list: 二维字符串列表，第一行为表头，后续为数据
    :param db_file: 输出的.db文件路径（如 "mydata.db"）
    :param table_name: 数据库中表的名称，默认 data_table
    """
    # 校验输入数据的合法性
    if not data_list or len(data_list) < 1:
        raise ValueError("二维列表不能为空，且至少包含表头行")

    # 提取表头和数据
    headers = data_list[0]  # 第一行作为列名
    rows = data_list[1:]  # 剩余行作为数据

    # 校验所有行的列数是否和表头一致
    col_count = len(headers)
    for idx, row in enumerate(rows):
        if len(row) != col_count:
            raise ValueError(f"第 {idx + 2} 行数据列数（{len(row)}）与表头列数（{col_count}）不一致")

    try:
        # 1. 连接数据库（不存在则自动创建）
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # 2. 动态生成创建表的SQL语句（所有列设为TEXT类型，因为输入都是字符串）
        # 处理列名中的特殊字符（如空格、符号），用双引号包裹
        columns = [f'"{header}" TEXT' for header in headers]
        create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(columns)})'
        cursor.execute(create_table_sql)

        # 3. 批量插入数据（参数化查询，避免SQL注入，提升效率）
        if rows:
            # 生成占位符 (?, ?, ...)，数量匹配列数
            placeholders = ', '.join(['?'] * col_count)
            insert_sql = f'INSERT INTO {table_name} VALUES ({placeholders})'
            # 批量执行插入（比逐行插入效率高）
            cursor.executemany(insert_sql, rows)

        # 4. 提交事务，确保数据写入文件
        conn.commit()
        print(f"成功！数据已写入 {db_file} 的 {table_name} 表中")
        print(f"表头：{headers}")
        print(f"数据行数：{len(rows)}")

    except sqlite3.Error as e:
        print(f"数据库操作出错：{e}")
        # 出错时回滚事务
        conn.rollback()
    finally:
        # 无论是否出错，都关闭游标和连接
        if cursor:
            cursor.close()
        if conn:
            conn.close()


data = read_xlsx_to_list(fr"35.xlsx")
data1 = read_xlsx_to_list(fr"35.xlsx",sheet_name="Sheet2")


list_to_sqlite_db(data_list=data1, db_file="智能药柜物联网系统.db", table_name="取药记录")
