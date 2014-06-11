#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <sys/time.h>
using namespace std;

void output(const char* val)
{
    ostringstream ostr;
    ostr << val;
    printf(ostr.str().c_str());
}

int main()
{
    /*
    stringstream ostr;
    ostr << "name: %s" << "xikangjie";
    cout << ostr.str() << endl;
    cout << ostr.str().c_str() << endl;
    string str1, str2;
    ostr >> str1 >> str2;
    cout << str1 << endl << str2 << endl;
    //printf(ostr.str().c_str());
*/
    char buf[256];
    struct timeval start, end;
    gettimeofday(&start, NULL);
    for (int i = 0; i < 1000; i++) {
        //ostringstream ostr;   // 4000us
        //ostr << "xiakngjie" << 123 << 123.123 << "asdfasdfasdfaksdjfklajslkdjflkjaskldjfklaskdjflkasjdf" << 2348923 << 1234.234 << endl;
        //printf(ostr.str().c_str());
        //ostr.str("");
        // 1000us
        //snprintf(buf, 256, "name: %s, sdfk %d, aksdjfkldjfklklaklsdjfljdkjalskdjfklasjdklfjlsdjfklajsdlfjklasdjfkl %f", "asdf", 123123, 123.123);
        if (true) {}    // 5us
    }
    gettimeofday(&end, NULL);
    int timeuse = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;
    printf("time: %d us\n", timeuse);
    
    output("what\n");


    return 0;
}
