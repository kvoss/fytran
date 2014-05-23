Simple Fortran interface
========================

A beginner Fortran developer is often puzzled with
the correct syntax of Fortran statements.
They just never stop surprising.

Writing little simple programs often can be helful but tedious.
This script simplifies this process.
It maintains a list of FORTRAN statements, and:
* generates FORTRAN source file from a template
* compiles the file
* runs the file and display its output
* returns to the prompt
* uses readline library to provide history of input


Example
-------

    $ ./fytran
    !e OR !! - compile and execute expressions
    !l       - print expressions
    !d       - delete an expressions
    !c       - clear the list of expressions
    !q       - quit
    >>> dimension a(5)
    >>> dimension b(5)
    >>> a = [1, 2, 3, 4, 5]
    >>> b = [5, 4, 3, 2, 1]
    >>> print *, a * b
    >>> !!
        5.0000000000000000        8.0000000000000000        9.0000000000000000        8.0000000000000000        5.0000000000000000     



Remarks
-------
The FORTRAN template uses:

    implicit real*8 (a-h, o-z)

