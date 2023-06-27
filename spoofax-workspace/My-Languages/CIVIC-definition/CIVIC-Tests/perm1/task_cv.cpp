#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>

std::mutex m;
std::condition_variable cv;

int f1() {
    std::unique_lock<std::mutex> lock(m);
    cv.wait(lock);
    return 1;
}


int f2() {
    std::lock_guard<std::mutex> lock(m);
    cv.notify_all();
    return 3;
}


int main() {
    f1();
    f2();
}
