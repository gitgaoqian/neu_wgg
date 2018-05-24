该程序集实现外骨骼存储服务：云端主要有存储服务和读取服务，都是节点形式存在。
程序运行流程：
1 云端运行cloudserver3.py,实现用户认证，服务查询和具体服务操作。
2 机器人请求存储服务：1，运行采集节点data_publish_test.launch（参数为exo_id:=xx）2,运行bridge.py;3,运行client3.py （参数：1 store）
3 监控端监控服务：1，运行bridge3.py;2,运行client3.py (参数1 fetch);3,运行monitor3.py(参数 1)

注：为了实现节点图的清晰性，规定节点，话题的名称规则如下：
1 机器人采集节点： Exo_id,话题store_topic_id,云端存储节点：StoreService_id
2 云端读取节点：FetchServic_id,话题fetch_topic_id,监控节点：Monitor_id


env_publisher.py模拟发布环境信息
angle_publihser.py模拟发布关节角度信息
location_publisher.py模拟发布位置信息
data_publisher.py订阅了上述三个文件发布的环境和关节角度信息，并且将其统一发布出去

monitor2:
云端存在性能优化节点和监控节点，外骨骼端只需要发送一个标识外骨骼的number，然后云端会订阅外骨骼
发布的信息数据，并将信息存入数据库中已经建好的表：exo_table，并且在云端显示出监控面板


monitor3:
云端存在性能优化节点和数据服务节点和监控服务节点，外骨骼端发送一个标识外骨骼的number以及操作命令
store，云端会开启数据服务节点将信息存入数据库中．第三方用户发送一个标识外骨骼的number以及操作命令fetch,
云端会开启监控服务节点，读取数据库中相应外骨骼的信息，并且向外发布．用户开启监控面板．

2018-5-24：更改存储服务的URI形式
@app.route('/cloud_service/<robotID>/<action>',methods=['POST'])
改为：
@app.route('/storage/<robotID>/<action>',methods=['POST'])