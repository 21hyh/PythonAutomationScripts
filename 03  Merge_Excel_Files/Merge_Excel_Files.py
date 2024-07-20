import pandas as pd

# 读取第一个Excel文件的Sheet1
df1 = pd.read_excel('file1.xlsx', sheet_name='Sheet1')

# 读取第二个Excel文件的Sheet1
df2 = pd.read_excel('file2.xlsx', sheet_name='Sheet1')

# 合并两个DataFrame
merged_df = pd.concat([df1, df2], ignore_index=True)
#使用pd.concat函数将df1和df2两个DataFrame合并为一个新的DataFramemerged_df。参数ignore_index=True表示在合并时忽略原有的索引值，并重新生成新的索引

# 保存合并后的数据到新的Excel文件
merged_df.to_excel('merged_file.xlsx', index=False)
#将合并后的DataFramemerged_df写入一个新的Excel文件merged_file.xlsx中。参数index=False指示在写入Excel文件时不包括DataFrame的索引（行号）。
