# !/bin/bash


PWD_PATH=$(pwd)
ROOT_PATH=..

BUILD_DIR=${ROOT_PATH}/build

cd ${BUILD_DIR}

make

cd ${PWD_PATH}


echo "**************************"
echo "Percona-Server make Finish"
echo "**************************"