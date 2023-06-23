#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>

std::mutex m;
std::condition_variable cv;
std::promise<void> work_start_promise, work_done_promise;
bool work_done = false;

void worker_function() {
    auto work_start_future = work_start_promise.get_future();
    work_start_future.wait();
    std::cout << "In worker function: starting work\n";

    int x = 10;

    std::lock_guard<std::mutex> lock(m);
    work_done = true;
    cv.notify_all();
}

int f0() {
    std::thread worker_thread(worker_function);
    worker_thread.join();
    return 0;
}

int f1() {
    work_start_promise.set_value();
    return 1;
}

int f2() {
    std::unique_lock<std::mutex> lock(m);
    while(!work_done){
    cv.wait(lock);
    }
    return 2;
}

int f3() {
    work_done_promise.set_value();
    return 3;
}

int f4() {
    std::future work_done_future = work_done_promise.get_future();
    work_done_future.wait();
    return 4;
}

int main() {
    f0();
    f1();
    f2();
    f3();
    f4();
}

