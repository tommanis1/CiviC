#include <mutex>
std::mutex m;
bool f0(){
    
    return 11;
}

int f1(){
   return 0;
}

int main() {
    f0();
    f1();
}
