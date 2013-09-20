#!/usr/bin/env python

from pake import ifind, main, target, virtual


SRC = [path for path in ifind('.') if path.endswith('.py')]


virtual('all', 'pep8', 'pyflakes')


@target('pep8', SRC, help='runs pep8 on all source files', phony=True)
def pep8(t):
    t.run('pep8', '--ignore=E501', SRC)


@target('pyflakes', SRC, help='runs pyflakes on all source files', phony=True)
def pyflakes(t):
    t.run('pyflakes', SRC)


if __name__ == '__main__':
    main()
