#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.unlock();    m.unlock();    m.lock_shared();    m.lock_shared()
;
return 0;}