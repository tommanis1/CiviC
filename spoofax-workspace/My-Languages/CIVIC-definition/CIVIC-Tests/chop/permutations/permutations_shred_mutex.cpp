#include <iostream>
#include <exception>
#include <functional>#include <shared_mutex>

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

int main()
{std::cout << "block:0\n";
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4" << unlock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:0\n";
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:1\n";
try { std::cout << "4" << unlock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:2\n";
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4" << unlock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:3\n";
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4" << unlock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "4" << unlock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:5\n";
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4" << unlock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3" << lock_shared() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2" << unlock() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1" << lock() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;}
;}