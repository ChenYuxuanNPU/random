"""
用于从层叠的文件夹中提取文件
"""

import os
import shutil

directory_path = r'C:\Users\1012986131\Desktop\工作文件\评聘部\义务教育优质均衡发展区\2025.06.04 - 提交教师资格查询截图或证件扫描件证明材料\收集内容\测试'

# 获取目录下所有文件和子目录名
all_files = os.listdir(directory_path)

print(all_files)

# print(len(all_files))

count = 0
for item in all_files:
    extract_path = directory_path + rf"\{item}"

    print(extract_path)

    for files in os.listdir(extract_path):
        print(extract_path + r"\\" + files)
        count += 1

        shutil.copy(extract_path + r"\\" + files, os.path.join(r'C:\Users\1012986131\Desktop\工作文件\评聘部\义务教育优质均衡发展区\2025.06.04 - 提交教师资格查询截图或证件扫描件证明材料\收集内容\output', files))

    print("")

print(count)
