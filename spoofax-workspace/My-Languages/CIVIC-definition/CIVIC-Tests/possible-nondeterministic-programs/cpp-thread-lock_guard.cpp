// https://en.cppreference.com/w/cpp/thread/lock_guard
#include <thread>
#include <mutex>
#include <iostream>
 
int g_i = 0;
std::mutex g_i_mutex;  // protects g_i
 
void safe_increment(int id)
{
    const std::lock_guard<std::mutex> lock(g_i_mutex);
    ++g_i;
 
    std::cout << "g_i: " << g_i << "; in thread #"
              << id << '\n';
 
    // g_i_mutex is automatically released when lock
    // goes out of scope
}
 
int main()
{
    std::cout << "g_i: " << g_i << "; in main()\n";
 
    std::thread t1(safe_increment, 0);
    std::thread t2(safe_increment, 1);
 
    t1.join();
    t2.join();
 
    std::cout << "g_i: " << g_i << "; in main()\n";
}