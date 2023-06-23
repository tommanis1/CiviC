#include <iostream>
#include <exception>
#include <functional>
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
{std::cout << "block:0\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:0\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:1\n";
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:2\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:3\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:5\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;}
;return 0;}