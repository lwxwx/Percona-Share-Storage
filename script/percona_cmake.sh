# !/bin/bash


PWD_PATH=$(pwd)
ROOT_PATH=..

# echo ${PWD_PATH}
if [ ! -d "build" ]; then
  mkdir ${ROOT_PATH}/build
else
  echo '${ROOT_PATH}/build has created'
fi 

BUILD_DIR=${ROOT_PATH}/build

cd ${BUILD_DIR}

cmake ${ROOT_PATH}/percona-server/ -DDOWNLOAD_BOOST=1  -DWITH_BOOST=${ROOT_PATH}

cd ${PWD_PATH}

echo "**************************"
echo "Percona-Server Cmake Finish"
echo "**************************"

