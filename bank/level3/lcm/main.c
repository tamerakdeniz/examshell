unsigned int lcm(unsigned int a, unsigned int b)
{
    unsigned int x = a;
    unsigned int y = b;
    unsigned int remainder;

    if (!a || !b)
        return (0);
    while (y)
    {
        remainder = x % y;
        x = y;
        y = remainder;
    }
    return (a / x * b);
}
