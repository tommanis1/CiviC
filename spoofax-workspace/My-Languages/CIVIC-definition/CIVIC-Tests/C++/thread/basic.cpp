#include <thread>
#include <iostream>

int main()
{

    std::thread t;
    std::cout << !t.joinable();
  return 0;
}