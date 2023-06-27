#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
std::mutex m;
 
void foo(int id) 
{   
    m.lock();
    std::cout << id << std::endl;
    m.unlock();
}
 
int main()
{
    std::jthread t1{foo, 0};
    std::jthread t2{foo, 1};
    std::jthread t3{foo, 3};

}
