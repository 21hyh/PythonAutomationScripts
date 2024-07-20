# -*- coding: utf-8 -*-
from graphviz import Digraph

from graphviz import Digraph

dot = Digraph('Fall_Detection_System', comment='Fall Detection System Use Case Diagram')
dot.attr(dpi='900')  # 设置较高的DPI值
dot.attr('node', fontname="SimHei")  # 设置中文字体
dot.attr('edge', fontname="SimHei")

dot.node('system', 'YOLOV8跌倒检测系统', shape='rectangle', style='filled', color='lightblue2')
dot.node('UC1', '跌倒事件检测', shape='ellipse')
dot.node('UC2', '历史事件查询', shape='ellipse')

dot.node('A1', '监控摄像头', shape='plaintext')
dot.node('A2', '用户', shape='plaintext')

# 使用元组表示边
dot.edges([('A1', 'UC1'), ('UC1', 'system'), ('A2', 'UC2'), ('UC2', 'system')])

dot.edge('A1', 'UC1', label='输入视频流')
dot.edge('UC1', 'system', label='触发警报并记录')
dot.edge('A2', 'UC2', label='发起查询请求')
dot.edge('UC2', 'system', label='显示查询结果')

# 输出图像到指定文件
dot.render('Fall_Detection_System_Use_Case_Diagram', format='png', cleanup=True)

