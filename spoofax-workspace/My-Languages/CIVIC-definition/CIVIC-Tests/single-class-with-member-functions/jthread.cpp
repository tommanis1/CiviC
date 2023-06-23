#include <thread>
#include <iostream>
void foo() {
while(i<10){
    std::cout << i ;
    i = i + 1;
}
}
std::jthread t{foo}
int main() {
    t.join();
    t.detach)();
}
