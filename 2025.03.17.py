import os
from func import *

# 指定文件夹路径
folder_path = r"C:\Users\1012986131\Desktop\命题比赛试题"

for grade in ["八年级", "七年级"]:
    path1 = folder_path + rf"\{grade}"

    # 获取文件夹下所有文件名
    file_names = [f.split()[0] for f in os.listdir(path1)]

    # print(file_names)
    print(len(file_names))

    output = [[item] for item in file_names]

    save_excel(two_dimension_list=output, excel_name=grade)
