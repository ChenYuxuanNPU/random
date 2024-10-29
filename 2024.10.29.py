import pandas as pd


def read_xlsx(file_path: str, sheet_name: str = "Sheet1") -> list:
    # 读取Excel文件
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # print(df)

    # 将DataFrame转换为列表（每个元素是一行，行内是列表形式的数据）
    return df.values.tolist()


data_set = read_xlsx(file_path="2024.10.29/1.xlsx")

print(data_set)

school_name = ""
kind = ""

output = []
temp = [0, 0, 0, 0]

for data in data_set:

    if school_name == "":
        school_name = data[0]
        kind = data[1]
        temp = [data[0], data[1], 0, data[3]]

    elif school_name != data[0] or kind != data[1]:
        output.append(temp)
        temp = [0,0,0,0]

        school_name = data[0]
        kind = data[1]

        temp = [data[0], data[1], 0, data[3]]

    elif school_name == data[0] and kind == data[1]:
        if data[2] in ["  博士研究生","  硕士研究生","  本科"]:
            temp[2] += data[3]

    else:
        print("env1")

output.append(temp)

print("")
print(output)
