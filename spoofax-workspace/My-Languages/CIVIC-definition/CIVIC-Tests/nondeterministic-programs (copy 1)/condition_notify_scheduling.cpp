#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>

std::mutex m;
std::condition_variable cv;
bool ready = false;

void print_id(int id) {
    std::unique_lock lock{m};
    while (!ready) {
        cv.wait(lock);
    }
    // after the wait, we own the lock.
    std::cout << "id:" << id << "\n";
}

void go() {
    std::unique_lock lock{m};
    ready = true;
    cv.notify_all();
}

int main() {
    std::jthread t1{print_id, 1};
    std::jthread t2{print_id, 2};
    std::jthread t3{print_id, 3};
    std::jthread t4{print_id, 4};

//    std::this_thread::sleep_for(std::chrono::seconds(2)); 
    go();

    return 0;
}