import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        # 删除“一定按格式命名”
        new_filename = filename.replace("一定按格式命名", "")

        # 在汉字与数字之间添加“-”
        # 使用正则表达式识别汉字(\u4e00-\u9fff)与数字(\d)的边界
        new_filename = re.sub(r'(\u4e00-\u9fff)(\d)', r'\1-\2', new_filename)
        new_filename = re.sub(r'(\d)(\u4e00-\u9fff)', r'\1-\2', new_filename)

        # 重命名文件
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed '{filename}' to '{new_filename}'")

# 替换为你的文件夹路径，确保路径是正确的
directory_path = "D:/Schoolwork02/02-07     大三下/5   项目管理/实验/实验一/【副本23：15】软件项目管理未在实验课交的可交到这里"
rename_files(directory_path)
