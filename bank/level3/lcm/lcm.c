
unsigned int    lcm(unsigned int a, unsigned int b)
{
    unsigned int x;
    unsigned int y;
    unsigned int gcd;

    if (a == 0 || b == 0)
        return(0);
    x = a;
    y = b;
    while(y != 0)
    {
        gcd = y;
        y = x % y;
        x = gcd;
    }
    return ((a * b) / x);
}