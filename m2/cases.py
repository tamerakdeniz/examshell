"""Subject-based local fixtures. Arguments are passed literally, without a shell."""
from string import ascii_letters, ascii_lowercase, ascii_uppercase

PROGRAM = {}


def program(name, rows):
    PROGRAM[name] = [(args, result + '\n') for args, result in rows]


def unary(name, fn, inputs):
    program(name, [([], ''), *[([s], fn(s)) for s in inputs], (['one', 'two'], '')])


samples = ['', 'a', '  AbZ\t xy9!   ', 'ZaAz09']
for name, fn in {
    'first_word': lambda s: (s.split() or [''])[0],
    'last_word': lambda s: (s.split() or [''])[-1],
    'rev_print': lambda s: s[::-1],
    'repeat_alpha': lambda s: ''.join(c * (ord(c.lower()) - 96 if c in ascii_letters else 1) for c in s),
    'ulstr': str.swapcase,
    'epur_str': lambda s: ' '.join(s.split()),
    'expand_str': lambda s: '   '.join(s.split()),
}.items():
    unary(name, fn, samples)
for name, n in [('rotone', 1), ('rot_13', 13), ('alpha_mirror', None)]:
    target = ''.join(s[n:] + s[:n] if n else s[::-1] for s in (ascii_lowercase, ascii_uppercase))
    unary(name, lambda s: s.translate(str.maketrans(ascii_letters, target)), samples)
unary('camel_to_snake', lambda s: ''.join('_' + c.lower() if c.isupper() else c for c in s), ['word', 'aLongURL'])
unary('snake_to_camel', lambda s: s.split('_')[0] + ''.join(w.title() for w in s.split('_')[1:]), ['word', 'a_long_url'])
unary('rev_wstr', lambda s: ' '.join(reversed(s.split())), ['', 'one', 'one two three'])
program('rostring', [([], ''), (['  one\t two three  '], 'two three one'), (['abc', 'ignored'], 'abc'), (['  '], '')])
program('search_and_replace', [([], ''), (['banana', 'a', 'X'], 'bXnXnX'), (['abc', 'x', 'a'], 'abc'), (['aa', 'aa', 'z'], ''), (['aa', 'a', 'zz'], '')])
program('fizzbuzz', [([], '\n'.join(('fizz' * (n % 3 == 0) + 'buzz' * (n % 5 == 0)) or str(n) for n in range(1, 101)))])
for name in ('inter', 'union', 'wdmatch', 'hiddenp'):
    pairs = [('aba', 'xabya'), ('abc', 'cba'), ('', 'x'), ('aa!b', 'ab!b')]
    rows = [([], '')]
    for a, b in pairs:
        it = iter(b)
        match = all(c in it for c in a)
        result = {'inter': ''.join(dict.fromkeys(c for c in a if c in b)),
                  'union': ''.join(dict.fromkeys(a + b)), 'wdmatch': a if match else '',
                  'hiddenp': str(int(match))}[name]
        rows.append(([a, b], result))
    program(name, rows)
program('do_op', [([], ''), *[(['-17', op, '5'], str(result)) for op, result in zip('+-*/%', [-12, -22, -85, -3, -2])]])
program('paramsum', [(args, str(len(args))) for args in ([], [''], ['a'] * 12)])
for name, pairs in {
    'add_prime_sum': [('1','0'), ('2','2'), ('11','28'), ('-3','0')],
    'print_hex': [('0','0'), ('15','f'), ('4096','1000'), ('171','ab')],
    'fprime': [('1','1'), ('2','2'), ('60','2*2*3*5'), ('49','7*7')],
    'tab_mult': [(str(n), '\n'.join(f'{i} x {n} = {i*n}' for i in range(1,10))) for n in (3, 12)],
}.items():
    program(name, [([], '0' if name == 'add_prime_sum' else ''), *[([x], y) for x,y in pairs]])
program('pgcd', [([], ''), (['42','12'],'6'), (['5','7'],'1'), (['42','42'],'42')])
for name, value in [('str_capitalizer','  AbC'.lower().replace('a','A') + '\tX!\n42abc'),
                    ('rstr_capitalizer','  abC\tx!\n42abC')]:
    program(name, [([], ''), (['  aBC\tX!', '42ABC'], value), ([''], '')])

# A driver is compiled separately from the submission to exercise its public API.
DRIVERS = {}
FUNCTION = {}


def function(name, prototype, body, rows, preamble=''):
    DRIVERS[name] = ('#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n'
                     + preamble + '\n' + prototype + ';\nint main(int ac, char **v){\n'
                     + '(void)ac; (void)v;\n' + body + '\nreturn 0;\n}\n')
    FUNCTION[name] = [([str(x) for x in args], str(result)) for args, result in rows]


for name in ('print_bits','reverse_bits','swap_bits'):
    rows = []
    for n in [0,1,2,53,128,255]:
        bits = f'{n:08b}'
        rows.append(([n], {'print_bits':bits, 'reverse_bits':int(bits[::-1],2), 'swap_bits':int(bits[4:]+bits[:4],2)}[name]))
    stmt = name + '((unsigned char)atoi(v[1]))'
    function(name, ('void ' if name == 'print_bits' else 'unsigned char ') + name + '(unsigned char)',
             stmt+';' if name == 'print_bits' else 'printf("%d",'+stmt+');', rows)
function('ft_atoi','int ft_atoi(const char*)','printf("%d",ft_atoi(v[1]));',
         [([''],0), (['  \t-42x'],-42), (['+003'],3), (['--7'],0)])
function('ft_atoi_base','int ft_atoi_base(const char*,int)','printf("%d",ft_atoi_base(v[1],atoi(v[2])));',
         [(['-Af',16],-175), (['10110',2],22), (['238',4],11), (['0',10],0)])
function('is_power_of_2','int is_power_of_2(unsigned int)','printf("%d",is_power_of_2(strtoul(v[1],0,10)));',
         [([n],int(n>0 and n&(n-1)==0)) for n in (0,1,2,3,64,65,2147483648)])
function('ft_strcmp','int ft_strcmp(char*,char*)','int n=ft_strcmp(v[1],v[2]);printf("%d",(n>0)-(n<0));',
         [([a,b],(a>b)-(a<b)) for a,b in [('abc','abc'),('ab','abc'),('z','a'),('','')]])
for name, fn in [('ft_strspn',lambda c,b:c not in b),('ft_strcspn',lambda c,b:c in b),('ft_strpbrk',lambda c,b:c in b)]:
    pointer = name == 'ft_strpbrk'
    function(name, ('char *' if pointer else 'size_t ') + name+'(const char*,const char*)',
             'char *p=ft_strpbrk(v[1],v[2]);printf("%td",p?p-v[1]:-1);' if pointer else f'printf("%zu",{name}(v[1],v[2]));',
             [([a,b],next((i for i,c in enumerate(a) if fn(c,b)), -1 if pointer else len(a))) for a,b in
              [('abcad','bd'), ('abc','abc'), ('aaa',''), ('','x'),('abc','z')]])
function('ft_strrev','char *ft_strrev(char*)','if(ft_strrev(v[1])!=v[1])return 1; fputs(v[1],stdout);',
         [([s],s[::-1]) for s in ('','abc','abcd')])
function('ft_strdup','char *ft_strdup(char*)','char *p=ft_strdup(v[1]); if(!p || p==v[1])return 1; fputs(p,stdout);free(p);',
         [([s],s) for s in ('','42 Istanbul','a')])
function('lcm','unsigned int lcm(unsigned int,unsigned int)','printf("%u",lcm(atoi(v[1]),atoi(v[2])));',
         [([0,7],0),([6,8],24),([5,7],35),([4,4],4)])
array = 'int a[32]; for(int i=1;i<ac;i++)a[i-1]=atoi(v[i]);'
sets = [[],[-9],[-3,-1,-5],[3,0,3,-2,1]]
function('max','int max(int*,unsigned int)',array+'printf("%d",max(a,ac-1));',[(a,max(a,default=0)) for a in sets])
function('sort_in_tab','void sort_int_tab(int*,unsigned int)',array+'sort_int_tab(a,ac-1);for(int i=0;i<ac-1;i++)printf("%d ",a[i]);',
         [(a,''.join(f'{x} ' for x in sorted(a))) for a in sets])
for name in ('ft_range','ft_rrange'):
    rows=[]
    for a,b in [(1,4),(2,-3),(0,0)]:
        x,y=(a,b) if name=='ft_range' else (b,a)
        step=1 if y>=x else -1
        rows.append(([a,b],''.join(f'{n} ' for n in range(x,y+step,step))))
    function(name,'int *'+name+'(int,int)',f'int a=atoi(v[1]),b=atoi(v[2]);int *p={name}(a,b);for(int i=0;i<=abs(a-b);i++)printf("%d ",p[i]);free(p);',rows)
function('ft_itoa','char *ft_itoa(int)','char *p=ft_itoa(atoi(v[1]));fputs(p,stdout);free(p);',
         [([n],n) for n in [0,1,-42,2147483647,-2147483648]])
function('ft_split','char **ft_split(char*)','char **p=ft_split(v[1]);for(int i=0;p[i];i++){puts(p[i]);free(p[i]);}free(p);',
         [([s],''.join(w+'\n' for w in s.split())) for s in ('',' \t\n','a','  abc\tde\nf  ')])
nodes='t_list *h=NULL;for(int i=ac-1;i>=1;i--){t_list *p=malloc(sizeof *p);p->data=v[i];p->next=h;h=p;}'
header='#include "ft_list.h"\n'
function('ft_list_size','int ft_list_size(t_list*)',nodes+'printf("%d",ft_list_size(h));',[(x,len(x)) for x in ([],['a'],['a','b','a'])],header)
function('ft_list_foreach','void ft_list_foreach(t_list*,void (*)(void*))',nodes+'ft_list_foreach(h,visit);',
         [(x,''.join(s+'\n' for s in x)) for x in ([],['one'],['3','2','3'])],header+'static void visit(void *p){puts(p);}')
function('ft_list_remove_if','void ft_list_remove_if(t_list**,void*,int (*)(void*,void*))',
         nodes+'ft_list_remove_if(&h,"x",cmp);while(h){puts(h->data);h=h->next;}',
         [(x,''.join(s+'\n' for s in x if s!='x')) for x in ([],['x','x'],['x','a','x','b','x'],['a'])],
         header+'static int cmp(void *a,void *b){return strcmp(a,b);}')
function('sort_list','t_list *sort_list(t_list*,int (*)(int,int))',
         nodes.replace('i>=1','i>=2').replace('p->data=v[i]','p->data=atoi(v[i])')+
         'h=sort_list(h,atoi(v[1])?asc:desc);while(h){printf("%d ",h->data);h=h->next;}',
         [([asc,*a],''.join(f'{n} ' for n in sorted(a,reverse=not asc))) for asc in (0,1) for a in sets],
         '#include "list.h"\nstatic int asc(int a,int b){return a<=b;}static int desc(int a,int b){return a>=b;}')
function('flood_fill','void flood_fill(char**,t_point,t_point)',
         't_point size={(int)strlen(v[3]),ac-3},start={atoi(v[1]),atoi(v[2])};flood_fill(v+3,size,start);for(int i=3;i<ac;i++)puts(v[i]);',
         [([0,0,'aab','aba','baa'],'FFb\nFba\nbaa\n'),([2,1,'aab','abb'],'aaF\naFF\n'),([0,0,'x'],'F\n')],
         '#include "flood_fill.h"')
