#include <iostream>

using namespace std;

int gcd(int numeratorIn, int denominatorIn);

int main() {
    int numerator, denominator;
    cout << "Enter a numerator: ";
    cin >> numerator;
    cout << "Enter a denominator: ";
    cin >> denominator;

    int divisor = gcd(numerator, denominator);

    cout << numerator/divisor << " " << denominator/divisor << endl;

    return 0;
}

int gcd(int numeratorIn, int denominatorIn)
{
    if(denominatorIn == 0)
        return numeratorIn;
    else
        return gcd(denominatorIn, numeratorIn % denominatorIn);
};
