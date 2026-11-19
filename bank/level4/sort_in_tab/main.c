void sort_int_tab(int *tab, unsigned int size)
{
    unsigned int i = 1;
    unsigned int j;
    int value;

    while (i < size)
    {
        value = tab[i];
        j = i;
        while (j > 0 && tab[j - 1] > value)
        {
            tab[j] = tab[j - 1];
            j--;
        }
        tab[j] = value;
        i++;
    }
}
