// adapted from https://en.cppreference.com/w/cpp/atomic/atomic_ref/atomic_ref
#include <atomic>
#include <thread>
#include <vector>
#include <numeric>
#include <iostream>
 
void inc_atomically(std::vector<char>& data) {
    for (char& x : data) {
        std::atomic_ref<char> xx(x);
        ++xx;  // atomic read-modify-write
    }
}
 
void inc_directly(std::vector<char>& data) {
    for (char& x : data)
        ++x;
}
 
template<typename Func>
void test_run(Func Fun) {
    std::vector<char> data(10'000'000);
    {
        std::jthread j1{ Fun, std::ref(data) };
        std::jthread j2{ Fun, std::ref(data) };
        std::jthread j3{ Fun, std::ref(data) };
        std::jthread j4{ Fun, std::ref(data) };
    }
    std::cout << "sum = " << std::accumulate(data.begin(), data.end(), 0) << '\n';
}
 
int main() {
    test_run(inc_atomically);
    test_run(inc_directly);
}