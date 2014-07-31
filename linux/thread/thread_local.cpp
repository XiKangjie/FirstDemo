#include <pthread.h>
#include <unistd.h>
#include <stdio.h>

class Foo
{
public:
    static Foo& GetInstance()
    {
        static Foo f;
        return f;
    }
    static __thread int val;
};

__thread int Foo::val = 0;

void* tfun1(void* arg)
{
    printf("tfun1: %d\n", Foo::GetInstance().val);
    Foo::GetInstance().val = 1;
    printf("tfun1: %d\n", Foo::GetInstance().val);
}

void* tfun2(void* arg)
{
    printf("tfun2: %d\n", Foo::GetInstance().val);
    Foo::GetInstance().val = 2;
    printf("tfun2: %d\n", Foo::GetInstance().val);
}

int main()
{
    pthread_t t1, t2;

    pthread_create(&t1, NULL, tfun1, NULL);
    sleep(1);
    pthread_create(&t2, NULL, tfun2, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    return 0;
}
