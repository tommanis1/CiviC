#include <iostream>
#include <mutex>
#include <shared_mutex>
#include <thread>

std::shared_mutex mutex_;
unsigned int counter = 0;

void increment_and_print()
{
    int i = 0;
    while (i < 3)
    {
        mutex_.lock();
        ++counter;
        mutex_.unlock();

        mutex_.lock_shared();
        std::cout << std::this_thread::get_id() << ' ' << counter << '\n';
        mutex_.unlock_shared();

        ++i;
    }
}

int main()
{
    std::thread thread1(increment_and_print);
    std::thread thread2(increment_and_print);

    thread1.join();
    thread2.join();

    return 0;
}