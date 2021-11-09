# GRUPO 8 - LP - JAVASCRIPT

# MARGARITA MAWYIN
# RAFAEL MONTALVO
# WILLY MATEO


import ply.lex as lex

# 2 palabras reservadas del LP asignado a su proyecto
reserved = {
    'class': 'CLASS',
    'new': 'NEW',
    'break': 'BREAK',
    'function': 'FUNCTION',
    'else': 'ELSE',
    'catch': 'CATCH',
    'while': 'WHILE',
    'void': 'VOID',
    'const': 'CONST',
    'import': 'IMPORT',
    'default': 'DEFAULT',
    'continue': 'CONTINUE',
    'debugger': 'DEBUGGER',
    'for': 'FOR',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'delete': 'DELETE',
    'await': 'AWAT',
    'export': 'EXPORT',
    'if': 'IF',
    'var': 'VAR',
    'let': 'LET',
    'do': 'DO',
    'extends': 'EXTENDS',
    'case': 'CASE',
    'super': 'SUPER',
    'null': 'NULL'
}

# List of token names.   This is always required
tokens = (
             'NUMERO',
             'MAS',
             'MENOS',
             'MULT',
             'DIV',
             'LPAREN',
             'RPAREN',
             'FLOTANTE',
             'VARIABLE',
             'IGUAL',
             'MASIGUAL',
             'MENOSIGUAL',
             'MULTIGUAL',
             'DIVIGUAL',
             'MODIGUAL',
             'IGUALIGUAL',
             'NOIGUALQUE',
             'MAYORQUE',
             'MENORQUE',
             'MAYORIGUALQUE',
             'MENORIGUALQUE',
             'AND',
             'OR',
             'BOOLEAN',
             'STRING',
             'UNDEFINED',
             'SYMBOL',
             'BIGINT',
             'NUMBER',
             'BOOL',
         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_STRING= r'("[^"]*"|\'[^\']*\')'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BOOLEAN = r'(true|false)'
t_IGUAL = r'='
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'-='
t_MULTIGUAL = r'\*='
t_DIVIGUAL = r'\/='
t_MODIGUAL = r'%='
t_IGUALIGUAL = r'=='
t_NOIGUALQUE = r'\!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUALQUE = r'>'
t_MENORIGUALQUE = r'<='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NULL = r'null'


# t_ESTRUCTURACONTROL = r'(if|else)'

# t_VARIABLE = r'^(var |let| )[a-zA-Z]\d+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'([+-]?\d+(?:\.?\d*(?:[eE][+-]?\d+)?)?|0[bB][\b[01]+\b]{1,}|0[xX][0-9a-fA-F]+|-\d*\.?\d+|\d*\.?\d+)$'
    return t

def t_BOOL(t):
    r'true|false'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z]+\d*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'                    #para ignorar lo que no es importante
# t_ignore_nombre = ""
t_ignore_CM1 = r"//.*"              # t_ignore_nombre = ""
t_ignore_CM2 = r"^(\/\*).*(\*\/)$"


# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = 'var t = 0xfff'

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)