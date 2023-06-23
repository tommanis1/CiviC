#include <mutex>
std::mutex m;
bool f0(){
    return m.try_lock();
}

int f1(){
    m.unlock();
   return 0;
}

int main() {
    f0();
    f1();
}
