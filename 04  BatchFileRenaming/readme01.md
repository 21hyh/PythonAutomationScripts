#脚本目的是重命名指定目录下的所有文件，执行两个主要操作：移除文件名中的特定字符串（"一定按格式命名"）和在汉字与数字之间添加连字符（"-"）。

1. **导入必要的模块**：

   - `import os`：用于与操作系统交互，如文件路径操作和文件重命名。
   - `import re`：用于执行正则表达式相关的操作，此处用于检测和修改文件名中的特定模式。

2. **定义文件重命名函数**：

   ```
   python复制代码def rename_files(directory):
       for filename in os.listdir(directory):
           # 删除“一定按格式命名”
           new_filename = filename.replace("一定按格式命名", "")
   
           # 在汉字与数字之间添加“-”
           new_filename = re.sub(r'(\u4e00-\u9fff)(\d)', r'\1-\2', new_filename)
           new_filename = re.sub(r'(\d)(\u4e00-\u9fff)', r'\1-\2', new_filename)
   
           # 重命名文件
           os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
           print(f"Renamed '{filename}' to '{new_filename}'")
   ```

   - `os.listdir(directory)`：列出指定目录下的所有文件和子目录的名称。
   - `filename.replace("一定按格式命名", "")`：从文件名中删除指定的字符串。
   - `re.sub()`：使用正则表达式替换文本。这里用两次`re.sub()`来确保数字和汉字之间正确添加连字符。第一个表达式处理汉字后跟数字的情况，第二个处理数字后跟汉字的情况。
   - `os.rename()`：用于重命名文件。它需要原始文件的完整路径和新文件的完整路径作为参数。

3. **设置文件夹路径并调用函数**：

   ```
   python复制代码directory_path = "D:/Schoolwork02/02-07 大三下/5 项目管理/实验/实验一/【副本23：15】软件项目管理未在实验课交的可交到这里"
   rename_files(directory_path)
   ```

   - 设置`directory_path`为你想要重命名文件的目录。
   - 调用`rename_files`函数来执行重命名操作。