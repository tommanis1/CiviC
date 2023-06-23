include <thread>
include <iostream>
void foo(int a){
	std::cout<< "foo";
}

void bar(){
	std::cout<< "bar";
}


int main() {
std::thread t{foo, 0};

return 0;
}
