#include <thread>
#include <iostream>
std::thread t;

void foo(){
std::cout << "test";
}

void bar(){
std::cout << "in bar in";
std::thread t = std::thread{foo};
std::cout << "in bar in scope";
}

int main(){
bar();
std::cout << "in main in scope";
return 0;
}
