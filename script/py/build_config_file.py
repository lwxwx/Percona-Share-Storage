'''
@Author: wei
@Date: 2020-06-23 18:03:52
@LastEditors: Do not edit
@LastEditTime: 2020-06-24 20:17:38
@Description: file content
@FilePath: /Percona-Share-Storage/script/py/build_config_file.py
'''

import os
import sys
from configparser import ConfigParser

# @param config_path

if(len(sys.argv) < 2):
    config_path="./config.ini"
else:
    config_path=sys.argv[1]

cfg = ConfigParser()
if(os.path.exists(config_path) == False):
    cfg['build_env']={'build_dir':'',
                'out_dir':'',
                'port':'',
                'xcom_port':'',
    }
    cfg['run_env']={
        'run_user':'',
        'node_count':'',
        'group_name':'',
        'local_ip':'',
        'remote_peer_nodes':''
    }
    with open(config_path,'w') as configfile:
        cfg.write(configfile)