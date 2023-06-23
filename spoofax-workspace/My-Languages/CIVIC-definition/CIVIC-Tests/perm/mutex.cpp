#include <mutex>
std::mutex m;
bool f0(){
    m.lock();
    return 0;
}

int f1(){
    m.unlock();
   return 0;
}

int main() {
    f0();
    f1();
}
