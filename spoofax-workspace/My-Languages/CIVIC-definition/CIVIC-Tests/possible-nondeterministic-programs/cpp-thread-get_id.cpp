// https://en.cppreference.com/w/cpp/thread/get_id
#include <chrono>
#include <iostream>
#include <syncstream>
#include <thread>
using namespace std::chrono_literals;
 
void foo(int this_id)
{
 
    std::osyncstream(std::cout) << "thread " << this_id << " sleeping...\n";
 
    std::this_thread::sleep_for(500ms);
}
 
int main()
{
    std::jthread t1 {foo, 0};
    std::jthread t2 {foo, 1};
}