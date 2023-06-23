// https://en.cppreference.com/w/cpp/thread/mutex/lock
#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
int g_num = 0;  // protected by g_num_mutex
std::mutex g_num_mutex;
std::jthread t1;
std::jthread t2;

void slow_increment(int id) 
{
    for (int i = 0; i < 3; ++i) {
        g_num_mutex.lock(); 
        ++g_num;
        // note, that the mutex also syncronizes the output
        std::cout << "id: " << id << ", g_num: " << g_num << '\n';
        g_num_mutex.unlock();
 
//        std::this_thread::sleep_for(std::chrono::milliseconds(234));
    }
}
int f1(){
    t1 = std::jthread{slow_increment, 0};
//    t1.detach();
return 0;}

int f2(){
    t2 = std::jthread{slow_increment, 1};
//    t2.detach();
return 0;}

int f3(){
    t1.join();
return 0;}

int f4(){
    t2.join();
return 0;}

int reset() {
        g_num_mutex.lock(); 
        g_num = 0;
        g_num_mutex.unlock();
return 0;
}

int main()
{
f1();
f2();
f3();
f4();
reset();
}
