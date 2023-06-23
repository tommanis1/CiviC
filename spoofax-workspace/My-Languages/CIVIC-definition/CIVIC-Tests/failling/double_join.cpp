#include <thread>
#include <iostream>
void foo(int a){
	std::cout<< "foo";
}



int main() {
std::thread t{foo, 0};
t.join();
t.join();

return 0;
}
