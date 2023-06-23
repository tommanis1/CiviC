#include <shared_mutex>

std::shared_mutex m;

void lock()
{
    m.lock();
}

void unlock()
{
    m.unlock();
}

void lock_shared()
{
    m.lock_shared();
}

void unlock_shared()
{
    m.unlock_shared();
}

void f1()
{
    std::jthread thread(lock);
}

void f2()
{
    std::jthread thread(lock_shared);
}

void f3()
{
    std::jthread thread(unlock);
}

void f4()
{
    std::jthread thread(lock_shared);
}

int main()
{
    f1();
    f2();
    f3();
    f4();


}
