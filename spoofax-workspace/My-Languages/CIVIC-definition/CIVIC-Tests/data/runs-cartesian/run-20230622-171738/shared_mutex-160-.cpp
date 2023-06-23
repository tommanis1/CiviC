#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.lock_shared();    m.lock_shared();    m.lock();    m.lock()
;
return 0;}