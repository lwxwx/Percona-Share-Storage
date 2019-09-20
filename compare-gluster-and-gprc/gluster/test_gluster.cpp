//
// Created by rrzhang on 2019/9/15.
//
#include <iostream>
#include <cassert>
#include "file_system.h"
#include "profiler.h"
#include "string_util.h"
using namespace std;

int main(){

    string path("/home/rrzhang/share-storage/");
    int fd = FileSystem::OpenFile(path, "testfile");
    FileSystem::string_len = 4096;
    int rw_num = 100000;

    Profiler random_time;
    Profiler local_rw_time;
    Profiler total_time;

    std::string value;
    RandNum_generator rng(0, 255);
    total_time.Start();
    for (int i = 0; i < rw_num; i++) {
        random_time.Start();
        value = StringUtil::random_str(rng, FileSystem::string_len);
        random_time.Suspend();
        local_rw_time.Start();
        int rc = FileSystem::Write(fd, value);
        local_rw_time.Suspend();
        assert(0 == rc);
    }
    std::cout<< "Total write "<< rw_num << " items"<<std::endl;
    std::cout << "write random time : " << random_time.Seconds() << " seconds" << std::endl;
    std::cout << "write file time   : " << local_rw_time.Seconds() << " seconds" << std::endl;
    std::cout << "write total time  : " << total_time.Seconds() << " seconds" << std::endl;

    local_rw_time.Clear();
    total_time.Clear();

    total_time.Start();
    for (int i = 0; i < rw_num; i++) {
        local_rw_time.Start();
        int rc = FileSystem::ReadByIndex(fd, i, &value);
        local_rw_time.Suspend();
        assert(0 == rc);
    }
    std::cout<< "Total read "<< rw_num << " items"<<std::endl;
    std::cout << "read file time   : " << local_rw_time.Seconds() << " seconds" << std::endl;
    std::cout << "read total time  : " << total_time.Seconds() << " seconds" << std::endl;

    return 0;
}