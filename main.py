# GRUPO 8 - LP - JAVASCRIPT

# MARGARITA MAWYIN
# RAFAEL MONTALVO
# WILLY MATEO

# Por hacer/revisar:
# Symbol
# tipo undefined

import ply.lex as lex

# =========================================================================================
# Palabras reservadas.
# =========================================================================================
# Palabras reservadas fuertes.
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

# Palabras reservadas suaves.
reserved_soft = {
    'constructor': 'CONSTRUCTOR',
    'get': 'GET',
    'init': 'INIT',
    'set': 'SET',
    'public': 'PUBLIC',
    'interface': 'INTERFACE',
    'implements': 'IMPLEMENTS',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'package': 'PACKAGE'
}
# =========================================================================================



# =========================================================================================
# Tokens.
# =========================================================================================
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
# =========================================================================================



# =========================================================================================
# Expresiones regulares.
# =========================================================================================

t_LPAREN = r'\('
t_RPAREN = r'\)'

# Operadores matemáticos.
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'

# Operadores de asignación.
t_IGUAL = r'='
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'-='
t_MULTIGUAL = r'\*='
t_DIVIGUAL = r'\/='
t_MODIGUAL = r'%='

# Operadores de comparación.
t_IGUALIGUAL = r'=='
t_NOIGUALQUE = r'\!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='

# Operadores lógicos.
t_AND = r'\&\&'
t_OR = r'\|\|'

# Tipos de datos primitivos.
t_STRING= r'("[^"]*"|\'[^\']*\')'
t_NULL = r'null'
t_BIGINT = r'\d+n'

def t_NUMBER(t):
    r'([+-]?\d+(?:\.?\d*(?:[eE][+-]?\d+)?)?|0[bB][\b[01]+\b]{1,}|0[xX][0-9a-fA-F]+|-\d*\.?\d+|\d*\.?\d+)$'
    return t

def t_BOOLEAN(t):
    r'true|false'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_$][\w$]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'                    #para ignorar lo que no es importante
# t_ignore_nombre = ""
t_ignore_CM1 = r"//.*"              # t_ignore_nombre = ""
t_ignore_CM2 = r"^(\/\*).*(\*\/)$"

# Componente léxico no reconocido.
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)
# =========================================================================================



# =========================================================================================
# Construcción de lexer.
# =========================================================================================
# Entradas para el test
data = '''
var let t1posdat0s _nueva NuevaVariable $otranueva $_$0
0xfff 789.8 true false null "grupo 8" 9318471394913n
'''

lexer = lex.lex()
lexer.input(data)

# Comprobar búsqueda de tokens.
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
# =========================================================================================

