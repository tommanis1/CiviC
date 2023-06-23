// https://en.cppreference.com/w/cpp/atomic/atomic/operator_arith
#include <atomic>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <mutex>
#include <random>
#include <thread>
 
std::atomic<int> atomic_count{0};
std::atomic<int> atomic_writes{0};
 
constexpr int global_max_count{72};
constexpr int writes_per_line{8};
constexpr int max_delay{100};

 
int main()
{
    auto work = [](const char id)
    {
        for (int count{}; (count = ++atomic_count) <= global_max_count;) {
            std::this_thread::sleep_for(
                std::chrono::milliseconds(5));
 
            bool new_line{false};
            if (++atomic_writes % writes_per_line == 0) {
                new_line = true;
            }
            // print thread `id` and `count` value
            {
                static std::mutex cout_mutex;
                std::lock_guard m{cout_mutex};
                std::cout << "[" << id << "] " << std::setw(3) << count << " │ "
                          << (new_line ? "\n" : "") << std::flush;
            }
        }
    };
 
    std::jthread j1(work, 'A'), j2(work, 'B'), j3(work, 'C'), j4(work, 'D');
}