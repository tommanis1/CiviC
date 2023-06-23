#include <iostream>
#include <mutex>
std::mutex m;
bool f0(){
    m.lock();
    return 0;
}

int f1(){
    m.unlock();
   return 0;
}

int main() {
try { std::cout << "count:2,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:2,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:3,function:2,result:" << f1() <<std::endl; } catch (...) { std::cout << "count:3,function:2,result:" << "fail" <<std::endl;};
try { std::cout << "count:4,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:4,function:1,result:" << "fail" <<std::endl;};
try { std::cout << "count:5,function:1,result:" << f0() <<std::endl; } catch (...) { std::cout << "count:5,function:1,result:" << "fail" <<std::endl;}
;
return 0;}