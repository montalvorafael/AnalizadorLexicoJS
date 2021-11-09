# GRUPO 8 - LP - JAVASCRIPT

# MARGARITA MAWYIN
# RAFAEL MONTALVO
# WILLY MATEO


import ply.lex as lex

#Palabras reservadas JS
reserved = {
    'class' : 'CLASS',
    'var' : 'VAR',
    'new' : 'NEW',
    'break' : 'BREAK',
    'function' : 'FUNCTION',
    'else' : 'ELSE',
    'catch' : 'CATCH',
    'while' : 'WHILE',
    'void' : 'VOID',
    'const' : 'CONST',
    'import' : 'IMPORT',
    'null' : 'NULL',
    'let' : 'LET',
    'default' : 'DEFAULT',
    'continue' : 'CONTINUE',
    'debugger' : 'DEBUGGER',
    'for' : 'FOR',
    'return' : 'RETURN',
    'switch' : 'SWITCH',
    'delete' : 'DELETE',
    'await' : 'AWAT',
    'export' : 'EXPORT',
    'if' : 'IF',
    'var' : 'VAR',
    'do' : 'DO',
    'extends' : 'EXTENDS',
    'case' : 'CASE',
    'super' : 'SUPER',
}




# Error handling rule

#funciones
def t_BOOL(t):
    r'true|false'
    return t

def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

    # Build the lexer
lexer = lex.lex()

# Test it out
data = ''' var t = 1'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
  print(tok)

