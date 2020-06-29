'''
@Author: wei
@Date: 2020-06-24 20:06:22
@LastEditors: Do not edit
@LastEditTime: 2020-06-24 23:07:17
@Description: file content
@FilePath: /Percona-Share-Storage/script/py/percona_server_connect.py
'''
import os
import sys
from configparser import ConfigParser
import subprocess

#@param config_path
#@param node_no
config_path = "./config.ini"
node_no = int(sys.argv[1]);   #命令行后面要加节点编号，从0开始

cfg = ConfigParser()
cfg.read(config_path)

build_path = cfg.get("build_env","build_dir")
out_dir = cfg.get("build_env","out_dir")
port = int(cfg.get("build_env","port"))
node_count = int(cfg.get("run_env","node_count"))

mysql_config_path = out_dir+"/percona_" + str(port+node_no) + ".conf"
mysql_cfg = ConfigParser()
mysql_cfg.read(mysql_config_path)
mysql_user = mysql_cfg.get("client","user")
mysql_passwd = mysql_cfg.get("client","password")

# ${BUILD_DIR}/bin/mysql -h${MYSQL_IP} -u${MYSQL_USER}  -P${MYSQL_PORT}  -p
connect_command = build_path + "/bin/mysql -h" + "127.0.0.1" + " -u" + mysql_user + " -P" + str(port+node_no) + " -p"

subprocess.call("cat " + out_dir + "/percona_" + str(port+node_no) + "/percona_error.log | grep password",shell=True) #从log里面把临时密码提取出来
print("ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的新密码'") #进去之后先执行这个改一下密码
subprocess.call(connect_command,shell=True) #登录mysql 输入临时密码 进去之后子再改密码

