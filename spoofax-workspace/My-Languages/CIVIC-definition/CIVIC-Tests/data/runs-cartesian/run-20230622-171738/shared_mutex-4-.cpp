#include <iostream>
#include <shared_mutex>

std::shared_mutex m;
int main(){
    m.lock();    m.lock();    m.unlock();    m.lock()
;
return 0;}