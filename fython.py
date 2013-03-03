"""
Author: Krzysztof Voss kmv633@mail.usask.ca
"""

from string import Template
import subprocess
import readline
import sys

with open('template.tpl', 'r') as f:
    tpl = Template(f.read())
ofile_fn = 'output.f'
stmts = []

def process():
    stmts_txt = '\n'.join(stmts)
    tpl_txt = tpl.substitute({
        'statements' : stmts_txt,
    })
    return tpl_txt

def help_me():
    print 'available: Fortran/!eval (also !!)/!clear/!list/!help/!quit'

if __name__ == '__main__':

    #ss = ['a = 12' , 'b = 22' , 'c = mod(a, b)' , 'print *, c']
    #stmts.extend(ss)

    while True:
        while True:
            line = raw_input('>>> ')
            if line == '!eval' or line == '!!':
                break
            elif line == '!clear':
                stmts = []
            elif line == '!list':
                for s in stmts:
                    print s
            elif line == '!help':
                help_me()
            elif line == '!quit':
                sys.exit(0)
            else:
                stmts.append(' '*6 + line)

        code = process()
        with open(ofile_fn, 'w') as f:
            f.write(code)

        cmd = ['gfortran', ofile_fn ]
        p = subprocess.Popen(cmd)
        p.wait()

        cmd = ['./a.out']
        p = subprocess.Popen(cmd)
        p.wait()
