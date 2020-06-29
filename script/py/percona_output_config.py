'''
@Author: wei
@Date: 2020-06-23 19:04:40
@LastEditors: Do not edit
@LastEditTime: 2020-06-24 20:39:17
@Description: file content
@FilePath: /Percona-Share-Storage/script/py/percona_output_config.py
'''

import os
import sys
from configparser import ConfigParser
import subprocess

# @param config_path
config_path = "./config.ini" # sys.argv[1]


cfg = ConfigParser()
cfg.read(config_path)

build_path = cfg.get("build_env","build_dir")     #mysql的安装目录，环境目录啥的，好像也可以直接用
out_dir = cfg.get("build_env","out_dir")          #data目录放在这个下面
port = int(cfg.get("build_env","port"))           #端口号
xcom_port = int(cfg.get("build_env","xcom_port")) #xcom的端口号，现在用的不是xcom了，和上面的端口号不一样就行
#user = cfg.get("build","user")
mysqld_path=build_path+"/bin/mysqld"

node_count = int(cfg.get("run_env","node_count"))  #sys.argv[2] #有几个节点 1
group_name = cfg.get("run_env","group_name")       #"mmlp_group" #现在没啥用
local_ip = cfg.get("run_env","local_ip")           #"10.11.6.120" #本地ip
remote_peer_nodes = cfg.get("run_env","remote_peer_nodes")# 远程IP：port,...

if(remote_peer_nodes == ""):
    peer_nodes_str = ""
else:
    peer_nodes_str = remote_peer_nodes + ","

for j in range(0,node_count):                       #有几个节点端口号就依次递增
    peer_nodes_str = peer_nodes_str + local_ip + ":" + str(xcom_port+j)
    # if(j < node_count - 1 and node_count > 1):
    #     peer_nodes_str += ","
    peer_nodes_str += ","

print("Peer_Node_String = " + peer_nodes_str)

if(os.path.exists(out_dir) == False):
    os.mkdir(out_dir)

for i in range(0,node_count):
    out_dir_i = out_dir + "/percona_" + str(port+i)
    if(os.path.exists(out_dir_i) == False):
        os.mkdir(out_dir_i)
    config_i = out_dir+"/percona_" + str(port+i) + ".conf"
    if(os.path.exists(config_i) == False):
        #print("create mysql config file")
        mysql_config_i = ConfigParser()
        mysql_config_i["client"] = {
            "port":str(port+i),
            "socket":out_dir_i + "/data/percona.sock",
            "user" : "root",
            "password": "123"
        }
        peer_nodes_str_i = peer_nodes_str.replace(local_ip+":"+str(xcom_port+i)+",","")
        peer_nodes_str_i = peer_nodes_str_i.rstrip(",")     #删除字符串末尾的逗号
        #print(peer_nodes_str_i)
        mysql_config_i["mysqld"] = {
            "port":str(port+i),
            "socket":out_dir_i + "/data/percona.sock",
            "basedir": build_path,
            "datadir": out_dir_i + "/data/",
            "log-error": out_dir_i + "/percona_error.log",
            "pid-file" : out_dir_i + "/data/percona.pid",
            "multi_master_log_plugin_group_name": group_name,
            "multi_master_log_plugin_local_node": local_ip + ":" + str(xcom_port+i),
            "multi_master_log_plugin_peer_nodes": peer_nodes_str_i,
            "symbolic-links" : "0"
        }
        with open(config_i,'w') as configfile: #写配置文件
            mysql_config_i.write(configfile)
        a,b = subprocess.getstatusoutput(mysqld_path + " --defaults-file="+config_i + "  --initialize")#运行并返回结果
        print("result["+str(i)+"] = " + str(a))
        if(a != 0):     #0是正常的，输出错误信息
            print(b)
