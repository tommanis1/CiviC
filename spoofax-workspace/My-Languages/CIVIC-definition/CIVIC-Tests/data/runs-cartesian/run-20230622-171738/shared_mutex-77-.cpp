#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.unlock();    m.lock();    m.unlock_shared();    m.unlock()
;
return 0;}