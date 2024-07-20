from graphviz import Digraph

def create_flowchart():
    # 创建有向图，设置全局字体
    dot = Digraph(comment='国家级实验示范中心发展评价方法', format='png')
    dot.attr('node', fontname='SimHei')  # 设置节点使用的字体为黑体
    dot.attr('edge', fontname='SimHei')  # 设置边使用的字体为黑体
    dot.attr(size='30,30')  # 设置图像尺寸（英寸）
    dot.attr(dpi='1200')  # 设置每英寸点数，增加图像清晰度

    # 添加节点
    dot.node('A', '2018-2022年各示范中心数据汇入')
    dot.node('B', '现行指标体系的参考与改进')
    dot.node('C', 'AHP-EWM指标赋权方法引入')
    dot.node('D', 'AHP主观权重赋权')
    dot.node('E', 'EWM客观权重赋权')
    dot.node('F', '纳什均衡优化权重分配')
    dot.node('G', 'TOPSIS法计算得分与排序')
    dot.node('H', 'RSR法分档')
    dot.node('I', '综合性评价')

    # 添加边
    dot.edges(['AB', 'BC'])
    dot.edge('C', 'D', '主观赋权')
    dot.edge('C', 'E', '客观赋权')
    dot.edges(['DF', 'EF', 'FG', 'GH', 'HI'])

    # 输出图形
    dot.render('flowchart_example', cleanup=True)

    print("流程图已生成，文件名为：flowchart_example.png")

# 调用函数创建流程图
create_flowchart()
