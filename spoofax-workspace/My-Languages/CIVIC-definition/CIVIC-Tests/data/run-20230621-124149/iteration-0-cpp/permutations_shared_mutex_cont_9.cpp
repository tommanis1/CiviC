#include <iostream>
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
try { std::cout << "count:65,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:65,function:1,result:" << "fail" <<std::endl;}
;
return 0;}