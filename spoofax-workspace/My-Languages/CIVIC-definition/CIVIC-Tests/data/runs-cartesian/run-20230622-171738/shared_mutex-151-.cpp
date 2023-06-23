#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.lock_shared();    m.unlock();    m.unlock();    m.unlock_shared()
;
return 0;}