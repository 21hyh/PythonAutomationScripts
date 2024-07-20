import os
import shutil


def rename_files_and_copy(source_path, destination_path):
    # 遍历源路径下的所有子文件夹
    for folder_name in os.listdir(source_path):
        folder_path = os.path.join(source_path, folder_name)

        # 只处理文件夹
        if os.path.isdir(folder_path):
            # 获取子文件夹内的文件路径
            file_name = os.listdir(folder_path)[0]
            file_path = os.path.join(folder_path, file_name)

            # 获取原文件的后缀名
            file_extension = os.path.splitext(file_name)[1]

            # 新文件名为子文件夹名字加上"课程论文"，保留原后缀名
            new_file_name = folder_name + "_课程论文" + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)

            # 复制已重命名的文件到目标路径
            destination_file_path = os.path.join(destination_path, new_file_name)
            shutil.copy(new_file_path, destination_file_path)


# 源路径
source_path = "D:/30866/Desktop/【软件21-1班课程论文】软件体系结构 - 副本"
# 目标路径
destination_path = "D:/30866/Desktop/【软件21-1班】体系结构课程论文"

# 调用函数
rename_files_and_copy(source_path, destination_path)
