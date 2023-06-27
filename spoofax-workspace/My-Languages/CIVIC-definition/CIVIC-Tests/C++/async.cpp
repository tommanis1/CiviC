#include <future>
#include <iostream>

int calculate() {
    std::cout << "Calculating..." << std::endl;
    return 2 + 2;
}

void print_thread_id() {
    std::cout << "Thread id: " << std::this_thread::get_id() << std::endl;
}

int main() {
    
    std::future<int> result = std::async(calculate);

    std::cout << result.get() << std::endl;
    
    // test std::launch::deferred
    std::future<int> result = std::async(std::launch::deferred, calculate);

    std::cout << "Before get()" << std::endl;
    std::cout << result.get() << std::endl;
    std::cout << "After get()" << std::endl;
    

    //test std::launch::async is in new thread
    print_thread_id();
    
    std::future<void> result = std::async(std::launch::async, print_thread_id);

    result.get();

    return 0;


}