// adapted from https://en.cppreference.com/w/cpp/thread/mutex/lock
#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
int g_num = 0;  // protected by g_num_mutex
std::mutex g_num_mutex;
 
void slow_increment(int id) 
{

    std::cout << "";
    g_num_mutex.lock(); 
    g_num = g_num + 1;
    // note, that the mutex also syncronizes the output
    std::cout << "id:" << id << "\n";
    g_num_mutex.unlock();
}
 
int main()
{
    std::thread t1{slow_increment, 0};
    std::thread t2{slow_increment, 1};
    std::thread t3{slow_increment, 2};

    t1.join();
    t2.join();
    t3.join();

    return 0;

}