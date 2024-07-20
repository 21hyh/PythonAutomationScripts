# -*- coding: utf-8 -*-
from graphviz import Digraph

from graphviz import Digraph

# 创建一个有向图
dot_corrected = Digraph(comment='计算机视觉中的跌倒识别问题')
dot_corrected.attr('node', fontname="SimHei")  # 设置节点字体为黑体

# 添加节点
dot_corrected.node('A', '计算机视觉识别跌倒场景')
dot_corrected.node('B', '识别精度不足')
dot_corrected.node('C1', '光线干扰')
dot_corrected.node('C2', '人体被遮挡')
dot_corrected.node('C3', '视角变化')
dot_corrected.node('D', '关键特征提取困难')
dot_corrected.node('E', '平均精度mAP@0.5未达标')
dot_corrected.node('F', '需进一步提升精度')

# 添加边
dot_corrected.edge('A', 'B')
dot_corrected.edge('B', 'C1')
dot_corrected.edge('B', 'C2')
dot_corrected.edge('B', 'C3')
dot_corrected.edge('C1', 'D')
dot_corrected.edge('C2', 'D')
dot_corrected.edge('C3', 'D')
dot_corrected.edge('D', 'E')
dot_corrected.edge('E', 'F')

# 显示图表
dot_corrected.view()
