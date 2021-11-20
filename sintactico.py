import ply.yacc as yacc
from lexico import tokens
from lexico import lexer_js

# =========================================================================================
# Básico.
# =========================================================================================
start_rule = 'js'

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIV'),
)

def p_js(p):
    '''js : instrucciones
    | instrucciones js
    '''

def p_instrucciones(p):
    '''instrucciones : declaracion final_linea
    | asignacion final_linea
    | funcion
    | expresion final_linea
    | comparacion
    | logica
    | arreglo
    | map
    | if
    | switch
    | while
    | pop
    | push
    | mapSet
    '''

# Declaración =============================================================================
def p_declaracion_SinAsig(p):
    '''declaracion : VAR VARIABLE
    | LET VARIABLE
    | CONST VARIABLE
    '''

def p_declaracion_ConAsig(p):
    '''declaracion : VAR VARIABLE IGUAL tipos_datos
    | LET VARIABLE IGUAL tipos_datos
    | CONST VARIABLE IGUAL tipos_datos
    | VAR VARIABLE IGUAL comparacion
    | LET VARIABLE IGUAL comparacion
    | CONST VARIABLE IGUAL comparacion
    | VAR VARIABLE IGUAL expresion
    | LET VARIABLE IGUAL expresion
    | CONST VARIABLE IGUAL expresion
    '''

# Asignación ==============================================================================
def p_asignacion(p):
    '''asignacion : VARIABLE operadores_asig tipos_datos
    | VARIABLE IGUAL comparacion
    | VARIABLE IGUAL expresion
    | VARIABLE operadores_asig VARIABLE
    '''

# Expresión ===============================================================================
def p_expresion_mas(p):
    'expresion : expresion MAS term'
    # p[0] = p[1] + p[3]

def p_expresion_menos(p):     #NO SE PORQUE SALE SINTAXIS ERROR
    'expresion : expresion MENOS term'
    # p[0] = p[1] - p[3]

def p_expresion_comp(p):
    'comparacion : expresion operadores_comp term'

def p_expresion_log(p):
    'logica : expresion operadores_log term'

def p_expresion_term(p):
    'expresion : term'
    # p[0] = p[1]

# Return.
def p_expresion_return(p):
    '''expresion : RETURN expresion'''

# Termino =================================================================================
def p_term_mult(p):
    'term : term MULT factor'
    # p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIV factor'
    # p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    # p[0] = p[1]

# Factor ==================================================================================
def p_factor_var(p):
    'factor : VARIABLE'

def p_factor_num(p):
    'factor : tipos_datos'

def p_factor_expr(p):
    'factor : IZQPAREN expresion DERPAREN'

# Agrapaciones de datos y operadores ======================================================
def p_tipos_datos(p):
    '''tipos_datos : NUMBER
    | STRING
    | BOOLEAN
    | BIGINT
    | NULL
    | SYMBOL'''

def p_operadores_asig(p):
    '''operadores_asig : IGUAL
    | MASIGUAL
    | MENOSIGUAL
    | DIVIGUAL
    | MODIGUAL
    | MULTIGUAL'''

def p_operadores_comp(p):
    '''operadores_comp : MAYORQUE
    | MENORQUE
    | MAYORIGUALQUE
    | MENORIGUALQUE
    | NOIGUALQUE
    | IGUALIGUAL'''

def p_operadores_log(p):
    '''operadores_log : AND
    | OR'''

def p_final_linea(p):
    '''final_linea : FINALDELINEA
    | empty'''

def p_empty(p):
    'empty :'
    pass

# =========================================================================================


# =========================================================================================
# Funciones.
# =========================================================================================
# Encabezado
def p_funcion_enc(p):
    'funcion_enc : FUNCTION VARIABLE funcion_param'

# Parámetro.
def p_funcion_param(p):
    '''funcion_param : IZQPAREN parametros DERPAREN'''

def p_parametros(p):
    '''parametros : VARIABLE
    | VARIABLE COMA parametros
    | empty'''

def p_funcion(p):
    'funcion : funcion_enc IZQLLAVE js DERLLAVE'

# =========================================================================================


# =========================================================================================
# Estructuras condicionales.
# =========================================================================================
# If - if-else ============================================================================
def p_if(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
    | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE if'''

def p_if_else(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE'''

# Switch ==================================================================================
def p_switch(p):
    '''switch : SWITCH IZQPAREN VARIABLE DERPAREN IZQLLAVE ncasos DEFAULT DOSPUNTOS js DERLLAVE'''

def p_ncasos(p):
    '''ncasos : casos
    | casos ncasos
    '''

def p_casos(p):
    '''casos : CASE tipos_datos DOSPUNTOS js BREAK final_linea
    | CASE tipos_datos DOSPUNTOS'''

# While ===================================================================================
def p_while(p):
    '''while : WHILE IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE'''

# =========================================================================================


# =========================================================================================
# Estructuras de datos.
# =========================================================================================
# Array ===================================================================================
def p_arreglo(p):
    '''arreglo : VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE FINALDELINEA
    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL IZQCORCHETE DERCORCHETE FINALDELINEA
    | LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE FINALDELINEA
    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN FINALDELINEA
    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN FINALDELINEA
    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN FINALDELINEA
    | LET VARIABLE IGUAL IZQCORCHETE DERCORCHETE FINALDELINEA
    | VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE
    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN
    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN
    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN
    | VAR VARIABLE IGUAL IZQCORCHETE DERCORCHETE
    | LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE
    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN
    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN
    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN
    | LET VARIABLE IGUAL IZQCORCHETE DERCORCHETE '''

def p_lista(p):
    ''' lista : lista COMA lista
    | tipos_datos'''

# Métodos.
def p_pop(p):
    '''pop : VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN'''

def p_push(p):
    '''push : VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN'''

# Map =====================================================================================
def p_map(p):
    '''map : LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea
    | VAR VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea
    | CONST VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea'''

# Métodos.
def p_mapSet(p):
    '''mapSet : MAPLOWER PUNTO SET IZQPAREN tipos_datos COMA tipos_datos DERPAREN final_linea'''

# =========================================================================================


# =========================================================================================
# Error sintáctico.
# =========================================================================================
def p_error(p):
    print("Error de sintaxis.")
# =========================================================================================


# =========================================================================================
# Construcción del parser.
# =========================================================================================
parser_js = yacc.yacc(start=start_rule)

# Test ====================================================================================
# Ingreso por teclado.
# while True:
# try:
# text = input('calc > ')
# except EOFError:
# break
# if not text: continue
# result = parser_js.parse(text, lexer= lexer_js)
# print(result)

# Algoritmo de prueba
data = [
    # Declaración y asignacion.
    'var x;',
    'var _nueva = 0xfff;',
    'var pruebaE = 23e-8;',
    'var NuevaVariable = true;',
    'var $_$0 = "grupo 8";',
    'var sym1 = Symbol();',
    'var sym2 = Symbol("foo");',
    'let t1posdat0s = 789.8;',
    'let $otranueva = false;',
    'let pruebasNega = -789n;',

    # Estructuras de datos.
    'arreglo[0] = -893.2;',
    'let array = new Array()',
    'var nombres = new Array();',
    'var nombres = new Array(5);',
    'var nombres = new Array("Ana","Diana","Tom");',
    'var nombres = ["Ana","Diana","Tom"];',
    'var nombres = []; // arreglo vacío',
    'var eliminado = num.pop();',
    'var mascolores = colores.push("verde", "celeste");',
    'let expr = new Map();',
    'const expr2 = new Map()',
    'map.set("1", 2);',

    # Estructuras de control.
    '''
    if (9318471394913n > -200) {
        var varNum = 0b010010011110;
    }
    ''',
    '''
    if (num > num2) {
            minimo =num2
        } if (num > num3) {
            minimo=num3
        }
    ''',
    '''
    if (num2 > num) {
            num2=num2-num
        } if (num > num3) {
            num =num-num3
        } else {
            num=100
        }
    ''',
    '''
    while (n < 3) {
        x = n;
    }
    ''',
    '''
    switch (expr) {
        case 1:
            exp=12;
            break;
        case 2:
            exp2='hola';
            break;
        case 3:
        default:
            x=true;
    }
    ''',

    # Funciones
    '''
    function saludo(){
        exp='hola';
    }
    ''',
    '''
    function cuadrado(numero) {
        numero* numero;
    }
    ''',
    '''
    function newFunction(a, b, c) {
        let suma = a + b + c;
    }
    ''',
]

for instruccion in data:
    print(instruccion)
    result = parser_js.parse(instruccion, lexer= lexer_js)
    print(result)
    print()

# =========================================================================================

