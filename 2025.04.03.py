import os
import shutil


def flatten_folders(source_folder, target_folder):
    """
    将源文件夹中所有子文件夹的内容提取到目标文件夹

    参数:
        source_folder (str): 源文件夹路径(包含多个子文件夹的文件夹a)
        target_folder (str): 目标文件夹路径(所有内容将被移动到这里)
    """
    # 确保目标文件夹存在
    os.makedirs(target_folder, exist_ok=True)

    # 遍历源文件夹中的所有子文件夹
    for root, dirs, files in os.walk(source_folder):
        # 跳过源文件夹本身
        if root == source_folder:
            continue

        # 移动所有文件到目标文件夹
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(target_folder, file)

            # 处理文件名冲突
            if os.path.exists(dst_path):
                base, extension = os.path.splitext(file)
                counter = 1
                while os.path.exists(dst_path):
                    new_filename = f"{base}_{counter}{extension}"
                    dst_path = os.path.join(target_folder, new_filename)
                    counter += 1

            shutil.copy(src_path, dst_path)
            print(f"移动文件: {src_path} -> {dst_path}")

    print("所有文件移动完成！")


# 使用示例
if __name__ == "__main__":
    # 设置源文件夹路径(包含多个子文件夹的文件夹a)
    source_folder = r"C:\Users\1012986131\Desktop\工作文件\评聘部\教师数据采集\24spring\指导中心\石井2"

    # 设置目标文件夹路径
    target_folder = r"C:\Users\1012986131\Desktop\工作文件\评聘部\教师数据采集\24spring\指导中心\石井"

    flatten_folders(source_folder, target_folder)