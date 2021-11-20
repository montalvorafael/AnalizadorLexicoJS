import ply.yacc as yacc
from lexico import tokens
from lexico import lexer

# =========================================================================================
# Básico.
# =========================================================================================
start = 'js'

def p_js(p):
    '''js : instrucciones
        | instrucciones js'''

def p_instrucciones(p):
    '''instrucciones : declaracionVarSinAsig
                | asignacion
                | funcion
                | expresion
                | comparacion
                | arreglo
                | map
                | if
                | switch
                | pop
                | push
                | mapSet'''

def p_declaracionVarSinAsig(p):
    '''declaracionVarSinAsig : declarador VARIABLE
            | declarador VARIABLE FINALDELINEA'''

def p_asignacion(p):
    '''asignacion : VARIABLE operadoresAsig tipoDato
        | VARIABLE operadoresAsig tipoDato FINALDELINEA
        | VARIABLE IGUAL comparacion
        | VARIABLE IGUAL comparacion FINALDELINEA
        | VARIABLE IGUAL expresion
        | VARIABLE IGUAL expresion FINALDELINEA'''

def p_declarador(p):
    '''declarador : VAR
    | LET
    | CONST'''

def p_operadoresAsig(p):
    '''operadoresAsig : IGUAL
                        | MASIGUAL
                        | MENOSIGUAL
                        | DIVIGUAL
                        | MODIGUAL'''

def p_tipoDato(p):
    '''tipoDato : NUMBER
                | STRING
                | BOOLEAN
                | BIGINT
                | SYMBOL'''

def p_empty(p):
    'empty :'
    pass
# =========================================================================================


# =========================================================================================
# Funciones.
# =========================================================================================
# Un parámetro.
def p_funcion_unparametro(p):
    'funcion : FUNCTION VARIABLE IZQPAREN VARIABLE DERPAREN IZQLLAVE js DERLLAVE'
#function cuadrado (numero){ numero* numero };

# Sin parámetros.
def p_funcion_sinparametro(p):
    'funcion : FUNCTION VARIABLE IZQPAREN DERPAREN IZQLLAVE js DERLLAVE'
# function saludo (){ exp='hola' }
# =========================================================================================


# =========================================================================================
# Estructuras condicionales.
# =========================================================================================
# If - if-else.
def p_if(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
        | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE if'''

def p_if_else(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE'''

#if (num > num2) { minimo =num2} if (num > num3) { minimo=num3}
#if (num2 > num) { num2=num2-num} if (num > num3) { num =num-num3} else {num=100}

# Switch.
def p_switch(p):
    '''switch : SWITCH IZQPAREN VARIABLE DERPAREN IZQLLAVE ncasos DEFAULT DOSPUNTOS js DERLLAVE'''

def p_casos(p):
    '''casos : CASE tipoDato DOSPUNTOS asignacion BREAK FINALDELINEA
        | CASE tipoDato DOSPUNTOS'''

def p_ncasos(p):
    '''ncasos : casos
        | casos ncasos
    '''
#switch (expr) { case 1: exp=12; break; case 2: exp2='hola'; break; case 3: default: x=true; }

def p_comparacion(p):
    '''comparacion : VARIABLE comparador VARIABLE
            | expresion comparador expresion'''

def p_comparador(p):
    '''comparador : MAYORQUE
                | MENORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | NOIGUALQUE'''
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

    # var nombres = new Array();
    # var nombres = new Array(5);
    # var nombres = new Array("Ana","Diana","Tom");
    # var nombres = ["Ana","Diana","Tom"];
    # var nombres = []; // arreglo vacío


def p_lista(p):
   ''' lista : lista COMA lista
                | STRING
                | SYMBOL
                | NUMBER
                | BIGINT
                | BOOLEAN'''

# Métodos.
def p_pop(p):
    '''pop : VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN'''
#var eliminado = num.pop();

def p_push(p):
    '''push : VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN FINALDELINEA
    | VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN'''
#var mascolores = colores.push("verde", "celeste");


# Map =====================================================================================
def p_map(p):
    '''map : LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN
        | LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN FINALDELINEA
        | VAR VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN
        | VAR VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN FINALDELINEA
        | CONST VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN
        | CONST VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN FINALDELINEA'''
# let expr = new Map();
# const map = new Map()

# Métodos.
def p_mapSet(p):
    '''mapSet : MAPLOWER PUNTO SET IZQPAREN tipoDato COMA tipoDato DERPAREN
            | MAPLOWER PUNTO SET IZQPAREN tipoDato COMA tipoDato DERPAREN FINALDELINEA'''
# map.set('1', 2);

def p_expresion_mas(p):
    'expresion : expresion MAS term'

def p_expresion_menos(p):     #NO SE PORQUE SALE SINTAXIS ERROR
    'expresion : expresion MENOS term'

def p_expresion_term(p):
    'expresion : term'

def p_term_mult(p):
    '''term : term MULT factor
    | term MULT VARIABLE'''

def p_term_div(p):
    'term : term DIV factor'

def p_term_factor(p):
    'term : factor'

def p_factor_var(p):
    'factor : VARIABLE'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_expr(p):
    'factor : IZQPAREN expresion DERPAREN'
# =========================================================================================


# =========================================================================================
# Error sintáctico.
# =========================================================================================
def p_error(p):
    print("Error de sintaxis!")
# =========================================================================================


# =========================================================================================
# Construcción del parser.
# =========================================================================================
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
# =========================================================================================

