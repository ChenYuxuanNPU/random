import shutil
from pathlib import Path


def flatten_subfolders(source_dir, target_dir):
    """
    将源文件夹中所有一级子文件夹的内容提取到目标文件夹
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # 创建目标文件夹
    target_path.mkdir(parents=True, exist_ok=True)

    # 遍历一级子文件夹
    for subfolder in source_path.iterdir():
        if subfolder.is_dir():  # 确保是文件夹
            # 遍历子文件夹中的所有内容
            for item in subfolder.rglob('*'):
                if item.is_file():  # 只处理文件
                    # 生成新文件名（避免重名冲突）
                    relative_path = item.relative_to(subfolder)
                    new_filename = f"{subfolder.name}_{relative_path.name}"
                    new_filepath = target_path / new_filename

                    # 复制文件
                    shutil.copy2(item, new_filepath)
                    print(f"已复制: {item} -> {new_filepath}")


# 使用示例
if __name__ == "__main__":
    source_folder = "新建文件夹"  # 源文件夹路径
    target_folder = "新文件夹"  # 目标文件夹路径

    flatten_subfolders(source_folder, target_folder)
    print("操作完成！")
