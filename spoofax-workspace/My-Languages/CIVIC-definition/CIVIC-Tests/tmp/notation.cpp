#include <future>
int func(double) { return 0; }
int main() {
  std::packaged_task f{func}; // deduces packaged_task<int(double)>
  int i = 5;
  std::packaged_task g = [&](double) { return i; }; // deduces packaged_task<int(double)>
}
