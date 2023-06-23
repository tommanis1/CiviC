#include <mutex>
#include <condition_variable>
#include <future>

std::mutex m;
std::condition_variable cv;
int t() {return 10;}
std::packaged_task task{t};
std::promise<void> p;
bool ready = false;

int f0() {
    task();
    m.lock();
    ready = true;
    cv.notify_all();
    m.unlock();

    return task.get_future().get();
}

int f1() {
    m.lock();
    p.set_value();
    m.unlock();
    return 1;
}

int f2() {
    std::unique_lock l{m};
    while(!ready) {
        cv.wait(l);
    }
    // m.unlock();

    return 2;
}

int f3() {
    std::future f = p.get_future();
    f.wait();
    return 3;
}

int main() {
    f0();
    f1();
    f2();
    f3();
}