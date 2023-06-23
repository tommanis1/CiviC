#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>

void foo() {
std::cout << "1";
}
int main () {
std::cout << "0";
std::thread t{foo};
t.join();
std::cout << "2";
}
