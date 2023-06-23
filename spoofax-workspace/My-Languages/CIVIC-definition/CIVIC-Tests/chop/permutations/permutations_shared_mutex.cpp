#include <iostream>
#include <exception>
#include <functional>
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
{std::cout << "block:0\n";
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:0\n";
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:1\n";
try { std::cout << "4:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:2\n";
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:3\n";
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "4:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:5\n";
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f0() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;}
;return 0;}