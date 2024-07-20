from graphviz import Digraph

# 创建实施视图图形
dot = Digraph(comment='Implementation View of Fall Detection System', format='png', engine='dot')
dot.attr(dpi='900')
dot.attr('node', fontname='SimHei')  # 设置字体以显示中文
dot.attr('edge', fontname='SimHei')

# 定义各层及其组件
dot.node('InterfaceLayer', '界面层\nReact框架 & WebSockets', shape='component', style='filled', color='lightblue2')
dot.node('ServiceLayer', '服务层\nPython & Flask & OpenCV', shape='component', style='filled', color='lightblue2')
dot.node('DataAccessLayer', '数据访问层\nPostgreSQL & Entity Framework Core', shape='component', style='filled', color='lightblue2')
dot.node('InfrastructureLayer', '基础设施层\nDocker & Kubernetes & Nginx', shape='component', style='filled', color='lightblue2')

# 添加部署单元
dot.node('FrontEndApp', '前端应用\n静态资源服务器 & CDN', shape='folder', style='filled', color='yellow')
dot.node('UI', '用户界面\n单页应用(SPA) & Kubernetes', shape='folder', style='filled', color='yellow')
dot.node('VideoService', '视频处理服务\nGPU支持的微服务容器', shape='folder', style='filled', color='green')
dot.node('BusinessLogicService', '业务逻辑服务\n高可用性服务器群', shape='folder', style='filled', color='green')
dot.node('DatabaseServer', '数据库服务器\n高并发支持 & 定期备份', shape='folder', style='filled', color='red')
dot.node('CacheSystem', '缓存系统\nRedis & 主从复制', shape='folder', style='filled', color='red')
dot.node('LoadBalancer', '负载均衡器\nNginx & SSL解密', shape='folder', style='filled', color='purple')
dot.node('Security', '安全防护\nWAF & IDS', shape='folder', style='filled', color='purple')

# 添加层间关系
dot.edges([('InterfaceLayer', 'ServiceLayer'), ('ServiceLayer', 'DataAccessLayer'), ('DataAccessLayer', 'InfrastructureLayer')])
dot.edges([('InterfaceLayer', 'FrontEndApp'), ('InterfaceLayer', 'UI'), ('ServiceLayer', 'VideoService'), ('ServiceLayer', 'BusinessLogicService')])
dot.edges([('DataAccessLayer', 'DatabaseServer'), ('DataAccessLayer', 'CacheSystem')])
dot.edges([('InfrastructureLayer', 'LoadBalancer'), ('InfrastructureLayer', 'Security')])

# 输出图像
dot.render('./Implementation_View_Fall_Detection_System')

dot
