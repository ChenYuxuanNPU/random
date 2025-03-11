"""
问卷星数据的导出和统计(学生问卷数据)
"""
import openpyxl


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


data = read_xlsx_to_list(f'./学生问卷数据.xlsx')

start_flag = 0
end_flag = len(data[0]) - 1

output_count = {}
output_radio = {}

for i in range(len(data[0])):
    if "单选" in data[0][i]:
        start_flag = i
        break

for i in range(start_flag, len(data[0])):
    if "单选" not in data[0][i]:
        end_flag = i
        break

for i in range(start_flag, end_flag + 1):
    output_count[data[0][i]] = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    output_radio[data[0][i]] = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

print(start_flag)
print(end_flag)

for data_list in data:
    if "单选" in data_list[start_flag]:
        continue

    for i in range(start_flag, end_flag + 1):
        if data_list[i] in ["A", "B", "C", "D"]:
            output_count[f"单选{str(i-1)}"][data_list[i]] += 1

print(output_count)