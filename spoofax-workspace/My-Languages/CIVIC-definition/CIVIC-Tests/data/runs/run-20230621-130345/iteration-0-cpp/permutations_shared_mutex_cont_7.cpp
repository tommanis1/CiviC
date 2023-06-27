#include <iostream>
#include <shared_mutex>
std::shared_mutex m;
bool f0(){
    m.lock();
    return 0;
}

int f1(){
    m.unlock();
   return 0;
}

bool f2(){
    m.lock_shared();
    return 0;
}

int f3(){
    m.unlock_shared();
   return 0;
}

int main() {
try { std::cout << "count:43,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:43,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:44,function:3,result:" << f2() <<std::endl; } catch (...) { std::cout << "count:44,function:3,result:" << "fail" <<std::endl;};
try { std::cout << "count:45,function:3,result:" << f2() <<std::endl; } catch (...) { std::cout << "count:45,function:3,result:" << "fail" <<std::endl;};
try { std::cout << "count:46,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:46,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:47,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:47,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:48,function:4,result:" << f3() <<std::endl; } catch (...) { std::cout << "count:48,function:4,result:" << "fail" <<std::endl;};
try { std::cout << "count:49,function:4,result:" << f3() <<std::endl; } catch (...) { std::cout << "count:49,function:4,result:" << "fail" <<std::endl;};
try { std::cout << "count:50,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:50,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:51,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:51,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:52,function:3,result:" << f2() <<std::endl; } catch (...) { std::cout << "count:52,function:3,result:" << "fail" <<std::endl;};
try { std::cout << "count:53,function:3,result:" << f2() <<std::endl; } catch (...) { std::cout << "count:53,function:3,result:" << "fail" <<std::endl;};
try { std::cout << "count:54,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:54,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:55,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:55,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:56,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:56,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:57,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:57,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:58,function:4,result:" << f3() <<std::endl; } catch (...) { std::cout << "count:58,function:4,result:" << "fail" <<std::endl;};
try { std::cout << "count:59,function:4,result:" << f3() <<std::endl; } catch (...) { std::cout << "count:59,function:4,result:" << "fail" <<std::endl;};
try { std::cout << "count:60,function:3,result:" << f2() <<std::endl; } catch (...) { std::cout << "count:60,function:3,result:" << "fail" <<std::endl;};
try { std::cout << "count:61,function:3,result:" << f2() <<std::endl; } catch (...) { std::cout << "count:61,function:3,result:" << "fail" <<std::endl;};
try { std::cout << "count:62,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:62,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:63,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:63,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:64,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:64,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:65,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:65,function:1,result:" << "fail" <<std::endl;}
;
return 0;}