#include <shared_mutex>

std::shared_mutex m;

int f0()
{
    m.lock();
    return 0;
}

int f1()
{
    m.unlock();
    return 1;
}

int f2()
{
    m.lock_shared();
    return 2;
}

int f3()
{
    m.unlock_shared();
    return 3;
}

int main()
{
    f0();
    f1();
    f2();
    f3();
}
