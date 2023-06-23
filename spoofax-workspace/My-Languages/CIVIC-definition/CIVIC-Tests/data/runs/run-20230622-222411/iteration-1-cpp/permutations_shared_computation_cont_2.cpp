#include <iostream>
#include <future>
#include <iostream>
#include <mutex>
#include <thread>
#include <condition_variable>

std::mutex print_mtx;
std::mutex calc_mtx;
std::condition_variable cv;
bool ready = false;

void printThreadMsg(const std::string& msg){
    std::unique_lock<std::mutex> lck(print_mtx);
    std::cout << msg << std::endl;
}

void calculation1(std::promise<int>& prom){
    std::this_thread::sleep_for(std::chrono::seconds(1)); // Mimic a long calculation
    int result = 42;  // The result of a calculation
    prom.set_value(result);

    std::unique_lock<std::mutex> lck(calc_mtx);
    ready = true;
    cv.notify_all();
}

void calculation2(std::future<int>& fut){
    std::unique_lock<std::mutex> lck(calc_mtx);
    while (!ready) {
        cv.wait(lck);
    }
    
    int x = fut.get();
    printThreadMsg("Received: " + std::to_string(x));

    int y = x * 2;  // Another calculation
    printThreadMsg("Final Result: " + std::to_string(y));
}
std::promise<int> prom;
std::future<int> fut = prom.get_future();

int main(){
try { std::cout << "count:4 "; return 0 ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:5 "; return 0 ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:6 "; std::jthread t1(calculation1, std::ref(prom)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:7 "; std::jthread t1(calculation1, std::ref(prom)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:8 "; std::jthread t2(calculation2, std::ref(fut)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:9 "; std::jthread t2(calculation2, std::ref(fut)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:10 "; std::jthread t1(calculation1, std::ref(prom)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:11 "; std::jthread t1(calculation1, std::ref(prom)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:12 "; return 0 ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:13 "; return 0 ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:14 "; std::jthread t2(calculation2, std::ref(fut)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:15 "; std::jthread t2(calculation2, std::ref(fut)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:16 "; std::jthread t1(calculation1, std::ref(prom)) ;} catch (...) { std::cout << "fail" <<std::endl;};
try { std::cout << "count:17 "; std::jthread t1(calculation1, std::ref(prom)) ;} catch (...) { std::cout << "fail" <<std::endl;}
;
return 0;}