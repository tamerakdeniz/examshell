

#include <unistd.h>

void print_bits(unsigned char octet)
{
    int maxbits;
    unsigned char bit;
    maxbits = 8;
    while (maxbits--)
    {
        bit = (octet >> maxbits & 1) + '0';
        write(1, &bit, 1);
    }
}