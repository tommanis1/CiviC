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

int f2() {
    std::future f = task.get_future();
    int x = f.get();
    return x;
}


int f4() {
    task();
    return 4;
}

int main() {
    f2();
    f4();
}
