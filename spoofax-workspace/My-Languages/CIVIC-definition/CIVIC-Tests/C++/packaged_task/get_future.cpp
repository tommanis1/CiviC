#include <future>

int z() { return 0; }
int main()
{
  std::packaged_task p{z};
  std::future f = p.get_future();

  p();

  std::cout <<  p.valid();
  std::cout << f.get() == 0;
  return 0;
}
