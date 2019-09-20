//
// Created by rrzhang on 2019/9/15.
//

#include <chrono>
#include <thread>
#include <iostream>
#include "profiler.h"

using namespace std;
using namespace chrono;

int main() {

//    std::chrono::time_point<std::chrono::system_clock> start = std::chrono::system_clock::now();
//    std::this_thread::sleep_for(std::chrono::seconds(1));
//    std::chrono::time_point<std::chrono::system_clock> end = std::chrono::system_clock::now();
//
//    std::chrono::microseconds duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
//
//    start = std::chrono::system_clock::now();
//    std::this_thread::sleep_for(std::chrono::seconds(1));
//    end = std::chrono::system_clock::now();
//
//    duration += std::chrono::duration_cast<std::chrono::microseconds>(end - start);
//
//
//    cout << double(duration.count()) ; //* microseconds::period::num / microseconds::period::den << endl;

    Profiler profiler;

    for(int i = 0; i< 10; i++){
        profiler.Start();

        std::this_thread::sleep_for(std::chrono::microseconds(1000000));
        profiler.Suspend();
    }

    double micro = profiler.Seconds();

    cout<<micro<<endl;
    return 0;
}