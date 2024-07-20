# -*- coding: utf-8 -*-
from graphviz import Digraph

# 创建逻辑视图图形
dot = Digraph(comment='Process View of Fall Detection System', format='png', engine='dot')
dot.attr(dpi='300')
dot.attr('node', fontname='SimHei')  # 设置字体以显示中文
dot.attr('edge', fontname='SimHei')

# 添加进程节点
dot.node('ControlProcess', '主控制进程\n系统启动与监控', shape='box3d', style='filled', color='lightblue2')
dot.node('VideoProcess', '视频处理进程\n实时视频流分析', shape='box3d', style='filled', color='lightblue2')
dot.node('EventProcess', '事件处理进程\n警报生成与事件存储', shape='box3d', style='filled', color='lightblue2')
dot.node('CommunicationProcess', '通信进程\n内外部数据交换', shape='box3d', style='filled', color='lightblue2')
dot.node('LogMonitorProcess', '日志与监控进程\n系统日志与性能监控', shape='box3d', style='filled', color='lightblue2')

# 添加进程之间的关联
dot.edges([('ControlProcess', 'VideoProcess'), ('ControlProcess', 'EventProcess'), ('ControlProcess', 'CommunicationProcess'), ('ControlProcess', 'LogMonitorProcess')])
dot.edge('VideoProcess', 'EventProcess', label='跌倒检测信号')
dot.edge('EventProcess', 'CommunicationProcess', label='事件通知')
dot.edge('CommunicationProcess', 'LogMonitorProcess', label='状态信息')

# 输出图像
dot.render('./Process_View_Fall_Detection_System')
