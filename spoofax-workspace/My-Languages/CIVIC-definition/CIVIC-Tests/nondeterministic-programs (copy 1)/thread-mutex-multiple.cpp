// adapted from https://en.cppreference.com/w/cpp/thread/mutex/lock
#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
int g_num = 0;  // protected by g_num_mutex
std::mutex g_num_mutex;
 
void slow_increment(int id) 
{
    int i = 0;
    while(i<2)
    {
                i = i + 1;
        std::cout << "";
        g_num_mutex.lock(); 
        g_num = g_num + 1;
        // note, that the mutex also syncronizes the output
        std::cout << "id:" << id << "num:" << g_num << "\n";
        g_num_mutex.unlock();
 
         std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}

int main()
{
    std::thread t1{slow_increment, 0};
    std::thread t2{slow_increment, 1};
//    std::thread t3{slow_increment, 2};

    t1.join();
    t2.join();
//    t3.join();
    return 0;
}
