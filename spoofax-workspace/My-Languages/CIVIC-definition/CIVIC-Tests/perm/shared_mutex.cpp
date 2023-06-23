#include <shared_mutex>
std::shared_mutex m;
bool f0(){
    m.lock();
    return 0;
}

int f1(){
    m.unlock();
   return 0;
}

bool f2(){
    m.lock_shared();
    return 0;
}

int f3(){
    m.unlock_shared();
   return 0;
}

int main() {
    f0();
    f1();
    f2();
    f3();
}
