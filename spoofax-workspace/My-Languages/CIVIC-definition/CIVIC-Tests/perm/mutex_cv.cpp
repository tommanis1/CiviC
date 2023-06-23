#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>

int foo() {
    return 8;    
}
std::mutex m;
std::condition_variable cv;
std::packaged_task task{foo};

void f0() {
    std::lock_guard<std::mutex> lock(m);
    return 0;
}

void f1() {
    std::unique_lock<std::mutex> lock(m);
    cv.wait(lock);
    return 1;
}

void f2() {
    int x = task.get_future().get();
    return x;
}

void f3() {
    std::lock_guard<std::mutex> lock(m);
    cv.notify_all();
    return 3;
}

void f4() {
    task();
    return 4;
}

int main() {
    f0();
    f3();
    f1();
    f2();
    f4();
}
