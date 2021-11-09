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

# Error handling rule
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

