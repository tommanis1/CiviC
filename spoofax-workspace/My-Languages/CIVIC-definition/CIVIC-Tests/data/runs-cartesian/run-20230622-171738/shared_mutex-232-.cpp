#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.unlock_shared();    m.lock_shared();    m.lock_shared();    m.lock()
;
return 0;}