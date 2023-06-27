// adapted from https://en.cppreference.com/w/cpp/thread/mutex/lock
#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
void foo(int id) 
{
    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::cout << id;
    return;
}
 
int main()
{
    std::thread t1{foo, 0};
    std::thread t2{foo, 1};
    std::thread t3{foo, 2};

    t1.join();
    t2.join();
    t3.join();

    return 0;

}