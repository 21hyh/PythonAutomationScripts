from graphviz import Digraph

# 创建数据视图图形
dot = Digraph(comment='Data View of Fall Detection System', format='png', engine='dot')
dot.attr(dpi='900')
dot.attr('node', fontname='SimHei')  # 设置字体以显示中文
dot.attr('edge', fontname='SimHei')

# 定义数据模型节点
dot.node('EventData', '事件数据\nPostgreSQL', shape='cylinder', style='filled', color='lightblue2')
dot.node('VideoData', '视频数据\n文件系统 & 数据库索引', shape='cylinder', style='filled', color='lightblue2')
dot.node('UserData', '用户数据\n加密存储', shape='cylinder', style='filled', color='lightblue2')

# 数据访问和安全节点
dot.node('DataAccess', '数据访问层\nEntity Framework Core & DAO', shape='note', style='filled', color='yellow')
dot.node('DataBackup', '数据持久性和备份\n实时与定期备份', shape='note', style='filled', color='green')
dot.node('DataSecurity', '数据安全\n加密 & 访问控制 & 审计日志', shape='note', style='filled', color='red')

# 添加节点之间的关联
dot.edges([('EventData', 'DataAccess'), ('VideoData', 'DataAccess'), ('UserData', 'DataAccess')])
dot.edges([('DataAccess', 'DataBackup'), ('DataBackup', 'DataSecurity')])

# 输出图像
dot.render('./Data_View_Fall_Detection_System')

dot
