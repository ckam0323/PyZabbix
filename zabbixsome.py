import json
import requests

# use API document to cometure some

url = 'http://192.168.1.10/api_jsonrpc.php'
headers = {'Content-Type':'application/json-rpc'}
#######################################################
# 对于非隐私数据，可以直接请求
# data = {
#     "jsonrpc": "2.0",   # jsonrpc版本，固定的
#     "method": "apiinfo.version",  # 获取zabbix版本的方法
#     "params": [],  # 参数
#     "id": 101  # 随便写个数字，表示任务号
# }

# result
# {'jsonrpc': '2.0', 'result': '3.4.4', 'id': 101}
#######################################################
# 获取隐私数据，首先要进行认证，能过认证得到用户的token
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/user/login
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 66
# }

# result
#(wu1904) [root@room9pc01 zbskt]# python zabbixsome.py
#{'jsonrpc': '2.0', 'result': 'b31667e2d631fb88bc1981dd737ff20d', 'id': 66}
#######################################################
# 获取所有的主机信息
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/get
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "b31667e2d631fb88bc1981dd737ff20d", # up ganggang get
#     "id": 10
# }
#######################################################
# 删除主机
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/delete

# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10261"    # 待删除主机的ID号
#     ],
#     "auth": "b31667e2d631fb88bc1981dd737ff20d",
#     "id": 24
# }
#######################################################
# 获取Linux Servers组的信息
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/hostgroup/get
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "b31667e2d631fb88bc1981dd737ff20d",
#     "id": 24
# }
#######################################################
# 获取Template OS Linux模板信息
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/template/get
# data ={
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#             ]
#         }
#     },
#     "auth": "b31667e2d631fb88bc1981dd737ff20d",
#     "id": 24
# }
# 'templateid': '10001',
#######################################################
# 创建主机，名为newoweb，加入到Linux Servers组，
# 应用Template OS Linux模板
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/host/create
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "newoweb", # 主机名
        "interfaces": [         # 使用zabbix agent进行监控
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.11",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [      # 加入的组
            {
                "groupid": "2"
            }
        ],
        "templates": [       # 应用的模板
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,      # 资产清单
        "inventory": {
            "macaddress_a": "mac addr 1",
            "macaddress_b": "56768"
        }
    },
    "auth": "b31667e2d631fb88bc1981dd737ff20d",
    "id": 24
}

# (wu1904) [root@room9pc01 zbskt]# python zabbixsome.py
# {'jsonrpc': '2.0', 'result': {'hostids': ['10264']}, 'id': 24}

#######################################################
r = requests.post(url, headers=headers,
    data=json.dumps(data))
print(r.json())  # 主要看result的值