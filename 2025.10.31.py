import os
from typing import List

from func import *


def find_files_by_extension(folder_path: str, extension: str) -> List[str]:
    """
    查找指定文件夹下特定后缀的所有文件

    Args:
        folder_path: 文件夹路径
        extension: 文件后缀，如 '.txt', '.py' (需要包含点号)

    Returns:
        包含所有匹配文件绝对路径的列表
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"文件夹路径不存在: {folder_path}")

    if not os.path.isdir(folder_path):
        raise ValueError(f"提供的路径不是文件夹: {folder_path}")

    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(extension.lower()):
                absolute_path = os.path.abspath(os.path.join(root, file))
                file_paths.append(absolute_path)

    return file_paths


basic_route = fr"C:\Users\1012986131\Desktop\省测统计数据- 10.15\学生名单"

output = {item: [] for item in ["新市片", "永平片", "石井片", "江高镇", "人和镇", "太和镇", "钟落潭镇", ]}
subject_list = []

for item in find_files_by_extension(folder_path=basic_route, extension=".xlsx"):
    file_name = os.path.splitext(os.path.basename(item))[0]
    subject = file_name[:2]
    subject_list.append(subject)

    data = read_xlsx_to_list(file_path=basic_route + fr"\\{file_name}.xlsx")

    title = ["学科"] + data[0]

    for item in data[1:]:
        temp = [subject] + item
        output[item[3]].append(temp)


for key,value in output.items():
    for subject in subject_list:
        save_excel(two_dimension_list=[title] + [item for item in value if item[0] == subject],excel_name=f"指导中心下发数据/{key}/{subject}学生数据")
