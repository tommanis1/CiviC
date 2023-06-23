#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.unlock_shared();    m.unlock_shared();    m.unlock();    m.lock_shared()
;
return 0;}