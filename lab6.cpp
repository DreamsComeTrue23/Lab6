#include <iostream>

using namespace std;

double h_function(int n)
{
    if (n == 1)
    {
        return 1;
    }
    else
    {
        return 1.0 / n + h_function(n - 1);
    }
}

double h_function()
{
    int n;

    cout << "Enter n: ";
    cin >> n;

    return h_function(n);
}
