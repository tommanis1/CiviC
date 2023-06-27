#include <thread>
#include <iostream>
void f() { }

int main()
{
	std::thread t{f};
	std::cout << t.joinable() ;
	t.join();
	std::cout << !t.joinable() ;
  return 0;
}