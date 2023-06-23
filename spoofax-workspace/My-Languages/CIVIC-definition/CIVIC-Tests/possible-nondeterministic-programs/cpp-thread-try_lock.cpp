// adapted from https://en.cppreference.com/w/cpp/thread/try_lock
#include <mutex>
#include <vector>
#include <thread>
#include <iostream>
#include <functional>
#include <chrono>

std::mutex m;
std::mutex foo_count_mutex;
std::mutex bar_count_mutex;
std::mutex done_mutex;

void increment(int counter, const char* desc) {
    for (int i = 0; i < 10; ++i) {
        std::lock_guard<std::mutex> lock(m);
        counter = counter + 1;
        std::cout << desc << ": " << counter << '\n';
        lock.unlock();
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
}

void update_overall(int foo_count, int bar_count, int& overall_count, bool& done) {
    done_mutex.lock();
    while (!done) {
        done_mutex.unlock();
        if (foo_count_mutex.try_lock() && bar_count_mutex.try_lock()) {
            overall_count += foo_count + bar_count;
            foo_count = 0;
            bar_count = 0;
            std::cout << "overall: " << overall_count << '\n';
            foo_count_mutex.unlock();
            bar_count_mutex.unlock();
        }
        std::this_thread::sleep_for(std::chrono::seconds(2));
        done_mutex.lock();
    }
    done_mutex.unlock();
}

int main() {
    int foo_count = 0;
    int bar_count = 0;
    int overall_count = 0;
    bool done = false;

    std::thread increment_foo{increment, foo_count, "foo"};
    std::thread increment_bar{increment, bar_count, "bar"};

    std::thread update_overall_thread{update_overall, foo_count, bar_count, std::ref(overall_count), std::ref(done)};

    increment_foo.join();
    increment_bar.join();
    done_mutex.lock();
    done = true;
    done_mutex.unlock();
    update_overall_thread.join();

    std::cout << "Done processing\n"
              << "foo: " << foo_count << '\n'
              << "bar: " << bar_count << '\n'
              << "overall: " << overall_count << '\n';
}
