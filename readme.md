该程序集实现外骨骼存储服务：云端主要有存储服务和读取服务，都是节点形式存在。
程序运行流程：
1 云端运行cloudserver3.py,实现用户认证，服务查询和具体服务操作。
2 机器人请求存储服务：1，运行采集节点data_publish_test.launch（参数为exo_id:=xx）2,运行bridge.py;3,运行client3.py （参数：1 store）
3 监控端监控服务：1，运行bridge3.py;2,运行client3.py (参数1 fetch);3,运行monitor3.py(参数 1)

注：为了实现节点图的清晰性，规定节点，话题的名称规则如下：
1 机器人采集节点： Exo_id,话题store_topic_id,云端存储节点：StoreService_id
2 云端读取节点：FetchServic_id,话题fetch_topic_id,监控节点：Monitor_id