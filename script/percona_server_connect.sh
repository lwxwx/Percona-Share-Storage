# !/bin/bash

source ./percona_build_env.sh

${BUILD_DIR}/bin/mysql -u root -p'123456' -P9898 -h127.0.0.1
