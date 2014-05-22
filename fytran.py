#!/usr/bin/python
"""
Author: Krzysztof Voss <shobbo@gmail.com>
"""

from string import Template
from subprocess import call
from sys import exit
import readline


COMPILER = ['gfortran', '-g', '-Wall']

CMDS = """!e OR !! - compile and execute expressions
!l       - print expressions
!d       - delete an expressions
!c       - clear the list of expressions
!q       - quit"""


program_tpl = """\
      program test
      implicit real*8 (a-h, o-z)
 
${statements}
 
      end program
"""
tpl = Template(program_tpl)
ofile_fn = 'output.f'
stmts = []

def process():
    stmts_txt = '\n'.join(stmts)
    tpl_txt = tpl.substitute({
        'statements' : stmts_txt,
    })
    return tpl_txt

def print_stm():
    for idx, s in zip(range(len(stmts)), stmts):
        print idx,':',s

def help_me():
    print 'available: Fortran/!!/!c/!d/!l/!h/!q'


def main():
    print CMDS
    while True:
        while True:
            line = raw_input('>>> ')
            if line == '!e' or line == '!!':
                break
            elif line == '!c':
                stmts = []
            elif line == '!l':
                print_stm()
            elif line == '!d':
                print_stm()
                idx = int(raw_input('idx to delete: '))
                stmts.pop(idx)
            elif line == '!h':
                help_me()
            elif line == '!q':
                exit(0)
            else:
                stmts.append(' '*6 + line)

        code = process()
        with open(ofile_fn, 'w') as f:
            f.write(code)
        try:
            ret = call(COMPILER + list(ofile_fn))
        except OSError as e:
            print "[!] Problem while running compiler"
            print "[!] OS error({0}): {1}".format(e.errno, e.strerror)
            print "[!] Check if {0} is instaled".format(COMPILER[0])
            exit(1)
            
        if ret == 0:
            cmd = ['./a.out']
            try:
                ret = call(cmd)
            except OSError as e:
                print "Problem with running application"
                print "[!] OS error({0}): {1}".format(e.errno, e.strerror)


if __name__ == '__main__':
    main()
