#include <mutex>
#include <iostream>
#include <system_error>
#include <shared_mutex>
std::mutex m;
void foo(int a){
	std::cout<< "foo";
}



int main() {
//    try
//    {
//
//
//m.lock();
//m.lock();
//}
//    catch (const std::system_error& ex)
//    {
//      std::cout << (ex.code() == std::make_error_code(std::errc::resource_deadlock_would_occur));
//    }

foo(0);

  typedef std::shared_mutex mutex_type;
  typedef std::shared_lock<mutex_type> lock_type;


//  try
//    {
//        std::shared_mutex m;
//      std::shared_lock <std::shared_mutex> lk{m};
//        m.lock();
//
//    } catch (const std::system_error& ex)
//
//    {
//      std::cout << (ex.code() == std::make_error_code(std::errc::resource_deadlock_would_occur));
//    }
//
//        mutex_type m;
//        m.lock();
//        m.lock();
//      lock_type l(m);
//
//	  l.lock();

    std::mutex mut;
//    std::unique_lock llk{mut};
    mut.lock();
    mut.lock();
      // Lock already locked shared_lock.
//      try
//	{

//	}
//      catch (const std::system_error& ex)
//	{
//	  std::cout << ( ex.code() == std::make_error_code
//		  (std::errc::resource_deadlock_would_occur) );
//	}


return 0;
}
