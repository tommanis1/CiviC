#include <iostream>
#include <thread>
#include <iostream>
void foo() {
while(i<10){
    std::cout << i ;
    i = i + 1;
}
}
std::thread t{foo}
int main() {
    t.join();    t.detach)()
;
return 0;}