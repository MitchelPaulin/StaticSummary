#include <iostream>
#include <limits.h>
#include <string.h>
/*
This is a test file with some bad C++ code to test some of the static tools
*/

class test
{
public:
    int x = 1;
};

int z() { return 0; }

//bad form
using namespace std;

int main(int argc, char *argv[])
{
    //use unititialized variable
    int x;
    int arr[x];

    //overflow
    x = INT_MAX;
    x++;

    //lossy casting
    double pi = 3.14159268;
    float pi2 = (float)pi;

    //dereference bad pointer
    test *t = new test();
    delete (t);
    cout << t->x << endl;

    //bad use of copy
    char large[15] = "HELLO WORLD!!!";
    char small[5];
    strncpy(small, large, 15);

    //security, execute arbitrary stuff
    popen(argv[1], "r");

    //allocate some mem but never free it (mem leak)
    void *p = malloc(sizeof(int));

    //division by zero obfuscated
    int bad = 4 / z();

    //reinterpret cast, dangerous
    test* null = reinterpret_cast<test*>(large); 
}

//infinite recursion
int f()
{
    cout << "HERE";
    f();
}