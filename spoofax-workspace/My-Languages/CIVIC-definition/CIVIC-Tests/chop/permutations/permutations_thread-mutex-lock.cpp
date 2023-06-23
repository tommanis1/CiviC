#include <iostream>
#include <exception>
#include <functional>
// https://en.cppreference.com/w/cpp/thread/mutex/lock
#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
 
int g_num = 0;  // protected by g_num_mutex
std::mutex g_num_mutex;
std::jthread t1;
std::jthread t2;

void slow_increment(int id) 
{
    for (int i = 0; i < 3; ++i) {
        g_num_mutex.lock(); 
        ++g_num;
        // note, that the mutex also syncronizes the output
        std::cout << "id: " << id << ", g_num: " << g_num << '\n';
        g_num_mutex.unlock();
 
//        std::this_thread::sleep_for(std::chrono::milliseconds(234));
    }
}
int f1(){
    t1 = std::jthread{slow_increment, 0};
//    t1.detach();
return 0;}

int f2(){
    t2 = std::jthread{slow_increment, 1};
//    t2.detach();
return 0;}

int f3(){
    t1.join();
return 0;}

int f4(){
    t2.join();
return 0;}

int reset() {
        g_num_mutex.lock(); 
        g_num = 0;
        g_num_mutex.unlock();
return 0;
}

int main()
{std::cout << "block:0\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
std::cout << "block:1\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:2\n";
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:3\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:4\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
std::cout << "block:5\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
std::cout << "block:6\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:7\n";
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:8\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:9\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
std::cout << "block:10\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
std::cout << "block:11\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
std::cout << "block:12\n";
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
std::cout << "block:13\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
std::cout << "block:14\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
std::cout << "block:15\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:16\n";
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:17\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:18\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:19\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:20\n";
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:21\n";
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:22\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:23\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:24\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:25\n";
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:26\n";
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:27\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:28\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:29\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;};
try { std::cout << "5:" << reset() <<std::endl; } catch (const std::exception& e) { std::cout << "5" << "fail" <<std::endl;};
try { std::cout << "4:" << f4() <<std::endl; } catch (const std::exception& e) { std::cout << "4" << "fail" <<std::endl;};
std::cout << "block:30\n";
try { std::cout << "3:" << f3() <<std::endl; } catch (const std::exception& e) { std::cout << "3" << "fail" <<std::endl;};
try { std::cout << "2:" << f2() <<std::endl; } catch (const std::exception& e) { std::cout << "2" << "fail" <<std::endl;};
try { std::cout << "1:" << f1() <<std::endl; } catch (const std::exception& e) { std::cout << "1" << "fail" <<std::endl;}
;return 0;}