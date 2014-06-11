#include <pthread.h>

class Foo
{
public:
    static pthread_mutex_t mtx;
};
pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;
int main()
{
    Foo f;

    return 0;
}
