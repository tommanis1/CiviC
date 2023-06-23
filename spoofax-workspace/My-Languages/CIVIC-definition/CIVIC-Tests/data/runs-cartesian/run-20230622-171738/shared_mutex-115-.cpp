#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.unlock();    m.unlock_shared();    m.lock();    m.unlock_shared()
;
return 0;}