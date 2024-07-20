from graphviz import Digraph

def create_flowchart():
    # 创建有向图，设置全局字体和分辨率
    dot = Digraph(comment='5G广播电视图像传输方法', format='png')
    dot.attr('node', fontname='SimHei')  # 设置节点使用的字体为黑体
    dot.attr('edge', fontname='SimHei')  # 设置边使用的字体为黑体
    dot.attr(size='30,30')  # 设置图像尺寸（英寸）
    dot.attr(dpi='1200')  # 设置每英寸点数，增加图像清晰度

    # 添加节点
    dot.node('A', '时间卷积神经网络')
    dot.node('B', '构建链路干扰预测模型,预测多径通信链路干扰')
    dot.node('D', '动态调整JPEG压缩参数')
    dot.node('E', '动态调整LDPC编码参数')
    dot.node('F', '得到最优调制参数')
    dot.node('G', '实现高效稳定图像传输')

    # 添加边
    dot.edges(['AB'])
    dot.edge('B', 'D', '根据预测结果调整')
    dot.edge('B', 'E', '根据预测结果调整')
    dot.edges(['DF','EF', 'FG'])

    # 输出图形
    dot.render('5g_broadcast_tv_flowchart', cleanup=True)

    print("流程图已生成，文件名为：5g_broadcast_tv_flowchart.png")

# 调用函数创建流程图
create_flowchart()
