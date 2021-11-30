# GRUPO 8 - LP - JAVASCRIPT

# MARGARITA MAWYIN
# RAFAEL MONTALVO
# WILLY MATEO

import ply.lex as lex

# =========================================================================================
# Palabras reservadas.
# =========================================================================================
# Palabras reservadas fuertes.
resultado_lexema = []
reserved = {
    'class': 'CLASS',
    'new': 'NEW',
    'break': 'BREAK',
    'function': 'FUNCTION',
    'else': 'ELSE',
    'while': 'WHILE',
    'const': 'CONST',
    'default': 'DEFAULT',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'if': 'IF',
    'var': 'VAR',
    'let': 'LET',
    'case': 'CASE',
    'null': 'NULL',
    'Map' : 'MAP',
    'Array' : 'ARRAY',
    'Set': 'SET_ESTRUC',
    'console' : 'CONSOLE',
    'log' : 'LOG'

}
# =========================================================================================



# =========================================================================================
# Tokens.
# =========================================================================================
tokens = [
    'AND',
    'IZQPAREN',
    'DERPAREN',
    'DIV',
    'DERLLAVE',
    'IZQLLAVE',
    'IZQCORCHETE',
    'DERCORCHETE',
    'FINALDELINEA',
    'PUNTO',
    'DOSPUNTOS',
    'COMA',
    'VARIABLE',
    'IGUAL',
    'MASIGUAL',
    'MENOSIGUAL',
    'MAS',
    'MENOS',
    'MULT',
    'MODULO',
    'MULTIGUAL',
    'DIVIGUAL',
    'MODIGUAL',
    'IGUALIGUAL',
    'NOIGUALQUE',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUALQUE',
    'MENORIGUALQUE',
    'OR',
    'BOOLEAN',
    'STRING',
    'UNDEFINED',
    'SYMBOL',
    'BIGINT',
    'NUMBER',
    'PUSH_METODO',
    'POP_METODO',
    'ADD_METODO',
    'HAS_METODO',
    'SET_METODO',
    'GET_METODO',

] + list(reserved.values())

# =========================================================================================



# =========================================================================================
# Expresiones regulares.
# =========================================================================================
# Metodos de estructura de datos
t_PUSH_METODO = r'\.push'
t_POP_METODO = r'\.pop'
t_ADD_METODO = r'\.add'
t_HAS_METODO = r'\.has'
t_SET_METODO = r'\.set'
t_GET_METODO = r'\.get'

t_IZQPAREN = r'\('
t_DERPAREN = r'\)'
t_IZQLLAVE = r'\{'
t_DERLLAVE = r'\}'
t_IZQCORCHETE = r'\['
t_DERCORCHETE = r'\]'
t_FINALDELINEA = r'\;'
t_PUNTO = r'\.'
t_COMA = r'\,'

# Operadores matemáticos.
t_MAS = r'\+'
t_MENOS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'

# Operadores de asignación.
t_IGUAL = r'='
t_MASIGUAL = r'\+='
t_MENOSIGUAL = r'-='
t_MULTIGUAL = r'\*='
t_DIVIGUAL = r'\/='
t_MODIGUAL = r'%='
t_DOSPUNTOS = r':'

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
#t_STRING= r'("[^"]*"|\'[^\']*\')'
t_NULL = r'null'
def t_STRING(t):
    r'("[^"]*"|\'[^\']*\')'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_SYMBOL(t):
    r'Symbol\(\)|Symbol\("[^"]*"\)'
    return t


def t_BIGINT(t):
    r'-?\d+n'
    return t

def t_NUMBER(t):
    r'(0[bB][(0|1)+]{1,}|0[xX][0-9a-fA-F]+|[+-]?\d+[eE][+-]?\d+|-\d*\.?\d+|\d*\.?\d+)'
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
    t.lexer.lineno += t.value.count("\n")

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
var _nueva = 0xfff;
let t1posdat0s = 789.8;
var NuevaVariable = true;
let $otranueva = false;
var $_$0 = "grupo 8";
if (9318471394913n > -200) {
    var varNum = 0b010010011110;
}
while (n < 3) {
  n ++;
  x += n;
}
var pruebaE = 23e-8;
arreglo[0] = -893.2;
let pruebasNega = -789n;
var sym1 = Symbol();
var sym2 = Symbol("foo");
var x;
Array()
.push .pop .has .add //pl
"ESTO ES UNA CADENA"
console.log('hola')
'''

lexer_js = lex.lex()
lexer_js.input(data)
def analizar(data):
    global resultado_lexema
    lexer_js.input(data)
    resultado_lexema.clear()
    # Tokenize
    while True:
        tok = lexer_js.token()
        if not tok:
            break  # No more input
        print(tok)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Pos {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema
# Comprobar búsqueda de tokens.
while True:
    tok = lexer_js.token()
    if not tok:
        break  # No more input
    print(tok)
# =========================================================================================

