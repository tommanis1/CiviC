#include <thread>
#include <iostream>
void foo() {
int i = 0;
while(i<20){
    std::cout << i;
    i = i + 1;
}
}
int main () {
    std::thread t{foo};
    //permutate
    t.join();
//    t.join(); // will call terminate
    t.detach();
//    t.detach();
//    t.join();
//    t.join();
    return 0;
}
