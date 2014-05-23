Simple Fortran interface
========================

Beginner Fortran developers are often puzzled with
correctness of FORTRAN statements syntax.
These last just never stop surprising.

Writing little simple programs often can be helful but tedious.
This script simplifies this process.
It maintains a list of FORTRAN statements, and:
* generates FORTRAN source file from a template
* compiles the file
* runs the file and display its output
* uses readline library to provide history of input


Example
-------

    $ python -m fytran
    !!       - compile and execute expressions
    !l       - print expressions
    !d       - delete an expressions
    !c       - clear the list of expressions
    !u       - remove last stmt
    !q       - quit
    >>> print *, 'hello' world
    >>> !!
    fytran.f:4.22:
      print *, 'hello' world                                            
                      1
    Error: Syntax error in PRINT statement at (1)
    >>> !u
    >>> print *, 'hello'
    >>> !!
     hello
    >>> !q
    $


Remarks
-------
The FORTRAN template uses:

    implicit real*8 (a-h, o-z)
