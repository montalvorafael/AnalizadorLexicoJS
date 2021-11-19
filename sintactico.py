import ply.yacc as yacc
from lexico import tokens
from lexico import lexer

def p_js(p):
    '''js : instrucciones
        | instrucciones js'''

def p_instrucciones(p):
    '''instrucciones : declaracionVar
                | asignacion
                | funcion
                | expresion
                | comparacion
                | arreglo
                | map
                | if
                | switch
                | pop
                | push'''


def p_declaracionVar(p):
    '''declaracionVar : VAR VARIABLE IGUAL tipo
            | LET VARIABLE IGUAL tipo'''
def p_asignacion(p):
    '''asignacion : VARIABLE operadoresAsig tipo
        | VARIABLE operadoresAsig tipo FINALDELINEA'''
def p_operadoresAsig(p):
    '''operadoresAsig : IGUAL
                        | MASIGUAL
                        | MENOSIGUAL
                        | DIVIGUAL
                        | MODIGUAL'''


#*************************************FUNCIONES************************************************
#FUNCION QUE ACEPTA UN PARAMETRO SOLAMENTE
def p_funcion_unparametro(p):
    'funcion : FUNCTION VARIABLE IZQPAREN VARIABLE DERPAREN IZQLLAVE js DERLLAVE'
#function cuadrado (numero){ 5* 5 }

#FUNCION SIN PARAMETROS
def p_funcion_sinparametro(p):
    'funcion : FUNCTION VARIABLE IZQPAREN DERPAREN IZQLLAVE js DERLLAVE'
#function cuadrado (numero){ exp='hola' }

def p_tipo(p):
    '''tipo : NUMBER
                | STRING
                | BOOLEAN
                | BIGINT
                | SYMBOL'''

#*************************************CONDICIONESLES***********************************************
#CONDICIONALES IF y IF-ELSE
def p_if(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
        | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE if'''

def p_if_else(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE'''

#if (num > num2) { 4*4} if (num > num3) { 4*5}
#if (num > num2) { 4*4} if (num > num3) { 4*5} else {4*10}

#CONDICIONAL SWITCH
def p_switch(p):
    '''switch : SWITCH IZQPAREN VARIABLE DERPAREN IZQLLAVE ncasos DEFAULT DOSPUNTOS js DERLLAVE'''

def p_casos(p):
    '''casos : CASE tipo DOSPUNTOS asignacion BREAK FINALDELINEA
        | CASE tipo DOSPUNTOS'''

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

#***************************************ESTRUCTURAS DE DATOS con sus METODOS************************************
#ESTRUCTURA ARRAY
def p_arreglo(p):
    '''arreglo : VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE
                | LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE'''

def p_lista(p):
   ''' lista : lista COMA lista
                | STRING
                | SYMBOL
                | NUMBER
                | BIGINT
                | BOOLEAN'''
#let arreglo = ["Manzana", "Banana",false, 1, 0b01,555n]

#METODOS DE ARRAY
def p_pop(p):
    'pop : VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN FINALDELINEA'
#var eliminado = num.pop();

def p_push(p):
    'push : VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN FINALDELINEA'
#var mascolores = colores.push("verde", "celeste");

#Estructura MAP:

def p_map(p):
    '''map : LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN
        | LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN FINALDELINEA'''
# let expr = new Map();

def p_expresion_mas(p):
    'expresion : expresion MAS term'

def p_expresion_menos(p):     #NO SE PORQUE SALE SINTAXIS ERROR
    'expresion : expresion MENOS term'

def p_expresion_term(p):
    'expresion : term'

def p_term_mult(p):
    'term : term MULT factor'

def p_term_div(p):
    'term : term DIV factor'

def p_term_factor(p):
    'term : factor'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_expr(p):
    'factor : IZQPAREN expresion DERPAREN'


# Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
