'''
@Author: wei
@Date: 2020-06-24 20:03:20
@LastEditors: Do not edit
@LastEditTime: 2020-06-24 21:08:55
@Description: file content
@FilePath: /Percona-Share-Storage/script/py/percona_server_run.py
'''
import os
import sys
from configparser import ConfigParser
import subprocess

#@param config_path
config_path = "./config.ini"

cfg = ConfigParser()
cfg.read(config_path)

build_path = cfg.get("build_env","build_dir")
out_dir = cfg.get("build_env","out_dir")
port = int(cfg.get("build_env","port"))
node_count = int(cfg.get("run_env","node_count"))
run_user = cfg.get("run_env","run_user")

mysqld_safe_path =  build_path + "/scripts/mysqld_safe"

for i in range(0,node_count):
    out_dir_i = out_dir + "/percona_" + str(port+i)
    config_i = out_dir+"/percona_" + str(port+i) + ".conf"
    #a,b = subprocess.getstatusoutput(mysqld_safe_path + " --defaults-file=" + config_i + " --user=" + run_user + " &",shell=True)
    res = subprocess.Popen(mysqld_safe_path + " --defaults-file=" + config_i + " --user=" + run_user + " &",shell=True)
    #print("result["+str(i)+"] = " + str(a))
    #if(a != 0):
    print(res.communicate())