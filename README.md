Simple Fortran interface
========================

I wrote it, because as a beginner Fortran developer, I was often puzzled with
the correct syntax of Fortran statements.

Writing a lot of simple program often can be tedious and this script solves it
nicely for me.

Usage
-----

After running the command:

    ./fytran

, a prompt is displayed.

On the prompt you enter either a Fortran expression or a command.

Available commands:

    !e OR !! - compile and execute expressions in a list
    !l       - print the list of expressions
    !d       - delete an expressions
    !c       - clear the entire list of expressions
    !q       - quit the application


Fortran uses:

    implicit real*8 (a-h, o-z)

