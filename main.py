# GRUPO 8 - LP - JAVASCRIPT

# MARGARITA MAWYIN
# RAFAEL MONTALVO
# WILLY MATEO


import ply.lex as lex

#Palabras reservadas JS
reserved = {
    'class' : 'CLASS',
    'var' : 'VAR',
    'let' : 'LET',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'switch' : 'SWITCH',
    'for' : 'FOR',
    'return' : 'RETURN',
    'null' : 'NULL',
    'catch' : 'CATCH',
    'new' : 'NEW',
    'void' : 'VOID',
    'function' : 'FUNCTION',
    'const' : 'CONST',
    'import' : 'IMPORT',
    'default' : 'DEFAULT',
    'continue' : 'CONTINUE',
    'do' : 'DO',
    'delete' : 'DELETE',
    'extends' : 'EXTENDS',
    'case' : 'CASE',
    'super' : 'SUPER',
    'export' : 'EXPORT',
    'await' : 'AWAT',
    'break' : 'BREAK',
    'debugger' : 'DEBUGGER'

}