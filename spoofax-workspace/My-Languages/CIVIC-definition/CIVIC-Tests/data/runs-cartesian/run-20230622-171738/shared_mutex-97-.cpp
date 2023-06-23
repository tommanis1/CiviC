#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.unlock();    m.lock_shared();    m.lock();    m.unlock()
;
return 0;}