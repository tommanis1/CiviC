#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>

std::mutex m;
std::condition_variable cv;
std::packaged_task<int()> task;
int counter = 0;

void inc () {
    return counter * 2; 
} 


int f1() {
    std::unique_lock<std::mutex> lock(m);
    counter = counter + 1;

    cv.notify_all();
    return counter;
}


int f3() {
    std::packaged_task task{inc};
    task();
    std::future f = task.get_future()
    int x = f.get();
    return x;
    
}

void f4() {
    std::unique_lock<std::mutex> lock(m);
    ++counter;
    std::cout << "In f4: counter is now " << counter << "\n";
    cv.notify_all();
}

int main() {
    f0();
    f1();
    f2();
    f3();
    f4();
}
