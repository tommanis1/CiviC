#include <iostream>
#include <future>
#include <thread>

// A simple function
int calculate(int x, int y) {
    return x * y;
}

int main() {
    // Package the task
    std::packaged_task<int(int, int)> task(calculate);
    std::future<int> future = task.get_future();
    task(10, 20);
    std::cout << "Result: " << future.get() << std::endl;

    return 0;
}


