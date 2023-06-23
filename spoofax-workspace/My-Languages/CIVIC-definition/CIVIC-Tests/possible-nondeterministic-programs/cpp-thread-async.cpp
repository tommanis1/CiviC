#include <algorithm>
#include <future>
#include <iostream>
#include <mutex>
#include <numeric>
#include <string>
#include <vector>

std::mutex m;

void foo(int i, const std::string& str)
{
    std::lock_guard<std::mutex> lk(m);
    std::cout << str << ' ' << i << '\n';
}

void bar(const std::string& str)
{
    std::lock_guard<std::mutex> lk(m);
    std::cout << str << '\n';
}

int addTen(int i)
{
    std::lock_guard<std::mutex> lk(m);
    std::cout << i << '\n';
    return i + 10;
}


int main()
{

    // Calls foo(42, "Hello") with default policy:
    // may print "Hello 42" concurrently or defer execution
    auto a1 = std::async(foo, 42, "Hello");
    // Calls bar("world!") with deferred policy
    // prints "world!" when a2.get() or a2.wait() is called
    auto a2 = std::async(std::launch::deferred, bar, "world!");
    // Calls addTen(43); with async policy
    // prints "43" concurrently
    auto a3 = std::async(std::launch::async, addTen, 43);
    a2.wait();                     // prints "world!"
    std::cout << a3.get() << '\n'; // prints "53"
} // if a1 is not done at this point, destructor of a1 prints "Hello 42" here
