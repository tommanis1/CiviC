#include <iostream>
#include <thread>

void print() {
    int i = 0;
    while (true) {
        std::cout << i << std::endl;
        i=i+1;
    }
}

int main() {
    std::thread t(print);
    t.detach();

    // The main thread exits here without waiting for the detached thread to finish.
    return 0;
}