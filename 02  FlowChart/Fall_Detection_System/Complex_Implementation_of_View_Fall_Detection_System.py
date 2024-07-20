# -*- coding: utf-8 -*-
from graphviz import Digraph

# 创建更复杂的实施视图图
dot_complex_impl = Digraph(comment='Complex Implementation View of Fall Detection System', format='png')
dot_complex_impl.attr(dpi='900')
dot_complex_impl.attr('node', fontname='Microsoft YaHei')  # 将'SimHei'替换为您系统支持的中文字体
dot_complex_impl.attr('edge', fontname='Microsoft YaHei')

# 定义层和子系统
dot_complex_impl.node('ui_layer', '界面层\n(React, WebSockets)', shape='component')
dot_complex_impl.node('service_layer', '服务层\n(Python, Flask, OpenCV)', shape='component')
dot_complex_impl.node('data_access_layer', '数据访问层\n(PostgreSQL, Entity Framework Core)', shape='component')
dot_complex_impl.node('infrastructure_layer', '基础设施层\n(Docker, Kubernetes, Nginx)', shape='component')

# 添加子系统内部的节点和连接
# 界面层
dot_complex_impl.node('monitoring_ui', '监控界面\n(React)', shape='component')
dot_complex_impl.node('alert_system', '报警系统\n(WebSockets)', shape='component')
dot_complex_impl.edge('ui_layer', 'monitoring_ui', label='包含')
dot_complex_impl.edge('ui_layer', 'alert_system', label='包含')

# 服务层
dot_complex_impl.node('video_processing', '视频处理服务\n(OpenCV)', shape='component')
dot_complex_impl.node('fall_detection', '跌倒检测\n(YOLOV5)', shape='component')
dot_complex_impl.edge('service_layer', 'video_processing', label='包含')
dot_complex_impl.edge('service_layer', 'fall_detection', label='包含')

# 数据访问层
dot_complex_impl.node('database', '数据库服务器\n(PostgreSQL)', shape='component')
dot_complex_impl.node('cache', '缓存系统\n(Redis)', shape='component')
dot_complex_impl.edge('data_access_layer', 'database', label='包含')
dot_complex_impl.edge('data_access_layer', 'cache', label='包含')

# 基础设施层
dot_complex_impl.node('docker', 'Docker容器', shape='component')
dot_complex_impl.node('kubernetes', 'Kubernetes集群', shape='component')
dot_complex_impl.node('nginx', 'Nginx服务器', shape='component')
dot_complex_impl.edge('infrastructure_layer', 'docker', label='包含')
dot_complex_impl.edge('infrastructure_layer', 'kubernetes', label='包含')
dot_complex_impl.edge('infrastructure_layer', 'nginx', label='包含')

# 添加层间连接
dot_complex_impl.edge('monitoring_ui', 'video_processing', label='接口调用')
dot_complex_impl.edge('alert_system', 'fall_detection', label='触发警报')
dot_complex_impl.edge('video_processing', 'fall_detection', label='数据流')
dot_complex_impl.edge('fall_detection', 'database', label='事件记录')
dot_complex_impl.edge('database', 'cache', label='数据缓存')

# 输出图像
dot_complex_impl.render('./Complex_Implementation_View_Fall_Detection_System')

dot_complex_impl
