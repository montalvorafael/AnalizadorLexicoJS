import ply.yacc as yacc
from lexico import tokens
from lexico import lexer

def p_js(p):
    '''js : instrucciones
        | instrucciones js'''

def p_instrucciones(p):
    '''instrucciones : tipo
                | operadoresAsig
                | declaracionVar
                | asignacion
                | funcion
                | expresion
                | comparacion
                | arreglo
                | if
                | casos
                | switch'''

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

#FUNCION QUE ACEPTA UN PARAMETRO SOLAMENTE
def p_funcion_unparametro(p):
    'funcion : FUNCTION VARIABLE IZQPAREN VARIABLE DERPAREN IZQLLAVE js DERLLAVE'
#function cuadrado (numero){ 5* 5 }

#CONDICIONAL IF y IF-ELSE
def p_if(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
    | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE'''
#if (num > num2) { 4*4}
#if (num > mun2) { 4*4} else {4*4}

#Estructura de control switch
def p_switch(p):
    '''switch : SWITCH IZQPAREN VARIABLE DERPAREN IZQLLAVE casos DEFAULT DOSPUNTOS asignacion DERLLAVE'''

#switch (expr) { case 1: exp=12; break; case 2: exp2='hola'; break; case 3: default: x=true; }
def p_tipo(p):
    '''tipo : NUMBER
                | STRING
                | BOOLEAN
                | BIGINT
                | SYMBOL'''

def p_casos(p):
    '''casos : casos casos
        | CASE tipo DOSPUNTOS asignacion BREAK FINALDELINEA
        | CASE tipo DOSPUNTOS'''

def p_comparacion(p):
    '''comparacion : VARIABLE comparador VARIABLE
            | expresion comparador expresion'''

def p_comparador(p):
    '''comparador : MAYORQUE
                | MENORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | NOIGUALQUE'''
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
