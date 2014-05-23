from distutils.core import setup

CONFIG = {
    'name'             : 'fytran',
    'description'      : 'A simple REPL Fortran utility',
    'version'          : '0.2.0',

    'author'           : 'Krzysztof Voss',
    'author_email'     : 'k.voss@usask.ca',

    'license'          : 'BSD',
    'platforms'        : ['POSIX',],
    'keywords'         : 'FORTRAN, utility, REPL',
    'py_modules'       : ['fytran'],
    'url'              : 'https://github.com/kvoss/fytran',
    'download_url'     : 'https://github.com/kvoss/fytran',
    'classifiers'      : [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7', ],
    }


setup(**CONFIG)

