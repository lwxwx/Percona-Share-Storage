# !/bin/bash
#echo 'export PERCONA_BUILD_PATH="$HOME/percona_build"' >> ~/.bashrc 


source ./percona_build_env.sh


echo ${BUILD_DIR}
if [ ! -d "$BUILD_DIR" ]; then
  mkdir $BUILD_DIR
else
  echo "${ROOT_PATH}/build has created"
fi 


cd ${BUILD_DIR}

cmake ${ROOT_PATH}/percona-server/ -DDOWNLOAD_BOOST=1  -DWITH_BOOST=${ROOT_PATH}/

cd ${PWD_PATH}

echo "**************************"
echo "Percona-Server Cmake Finish"
echo "**************************"

