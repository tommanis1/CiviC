
#include <future>
#include <iostream>

void t0()
{
  std::promise<int> p1;
  std::future<int> f1 = p1.get_future();

  std::cout << f1.valid();

  p1.set_value(0);

  auto i = f1.get();
  std::cout << (i == 0);
}


void t1()
{
  std::promise<int&> p1;
  std::future<int&> f1 = p1.get_future();

  std::cout << f1.valid();

  int i1 = 0;
  p1.set_value(i1);
  auto i2 = f1.get();

  std::cout << !f1.valid();
  std::cout <<( i1 == i2 );
}

void t2()
{
  std::promise<void> p1;
  std::future<void> f1 = p1.get_future();

std::cout <<f1.valid() ;

  p1.set_value();
  f1.get();

   std::cout << !f1.valid() ;
}

int main()
{
  t0();
  t1();
  t2();

  return 0;
}
