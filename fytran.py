""" Simple FORTRAN REPL

Author: Krzysztof Voss <k.voss@usask.ca>
"""

from string import Template
from subprocess import call
from sys import exit
import readline

# magic
COMPILER = ['gfortran', '-g', '-Wall']

class FortranTemplate(Template):
    program_tpl = """\
      program test
      implicit real*8 (a-h, o-z)
 
      ${statements}
 
      end program
"""

    def __init__(self, stmts):
        Template.__init__(self, self.program_tpl)
        self.stmts = stmts

    def __str__(self):
        stmts_txt = '\n      '.join(self.stmts)
        tpl_txt = self.substitute({ 'statements' : stmts_txt, })
        return tpl_txt

class Source:
    src_fn = 'fytran.f'
    
    def __init__(self, stmts):
        self.src = str(FortranTemplate(stmts))

    def _write(self):
        with open(self.src_fn, 'w') as f:
            f.write(self.src)

    def _compile(self):
        try:
            ret = call(COMPILER + [self.src_fn])
            return ret
        except OSError as e:
            print "[!] Problem while running compiler"
            print "[!] OS error({0}): {1}".format(e.errno, e.strerror)
            print "[!] Check if {0} is instaled".format(COMPILER[0])
            exit(1)
        
    def run(self):
        self._write()
        #TODO: too ugly
        cmd = ['./a.out']
        if self._compile() == 0:
            try:
                ret = call(cmd)
            except OSError as e:
                print "Problem with running application"
                print "[!] OS error({0}): {1}".format(e.errno, e.strerror)


class Fytran():
    CMDS = """\
!!       - compile and execute expressions
!l       - print expressions
!d       - delete an expressions
!c       - clear the list of expressions
!u       - remove last stmt
!q       - quit"""

    def __init__(self):
        self.stmts = list()

    def _list(self):
        for idx, s in enumerate(self.stmts):
            print idx, ':', s

    def _help(self):
        #print 'available: Fortran/!!/!c/!d/!l/!h/!u/!q'
        print self.CMDS

    def run(self):
        print self.CMDS
        while True:
            while True:
                line = raw_input('>>> ')
                if line == '!e' or line == '!!':
                    s = Source(self.stmts)
                    s.run()
                elif line == '!c':
                    self.stmts = list()
                elif line == '!l':
                    self._list()
                elif line == '!d':
                    self._list()
                    idx = int(raw_input('idx to delete: '))
                    try:
                        self.stmts.pop(idx)
                    except IndexError:
                        pass
                elif line == '!h':
                    self._help()
                elif line == '!u':
                    try:
                        self.stmts.pop()
                    except IndexError:
                        pass
                elif line == '!q':
                    exit(0)
                else:
                    self.stmts.append(line)


if __name__ == '__main__':
    i = Fytran()
    i.run()

