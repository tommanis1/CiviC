#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.lock();    m.lock();    m.unlock_shared();    m.unlock_shared()
;
return 0;}