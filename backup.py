import ply.yacc as yacc
from lexico import tokens
from lexico import lexer

def p_js(p):
    '''js : instrucciones
        | instrucciones js'''

def p_instrucciones(p):
    '''instrucciones : asignacion
                | funcion
                | expresion
                | comparacion
                | arreglo
                | if
                | pop'''

def p_asignacion(p):
    '''asignacion : VAR IGUAL VARIABLE
            | LET IGUAL VARIABLE'''
#*****************FUNCIONES***********************
#FUNCION QUE ACEPTA UN PARAMETRO SOLAMENTE
def p_funcion_unparametro(p):
    'funcion : FUNCTION VARIABLE IZQPAREN VARIABLE DERPAREN IZQLLAVE js DERLLAVE'
#function cuadrado (numero){ 5* 5 }


#*********************CONDICIONESLES***********************
#CONDICIONALES IF y IF-ELSE
def p_if(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
        | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE if'''

def p_if_else(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE'''

#if (num > num2) { 4*4} if (num > num3) { 4*5}
#if (num > num2) { 4*4} if (num > num3) { 4*5} else {4*10}


def p_comparacion(p):
    '''comparacion : VARIABLE comparador VARIABLE
            | expresion comparador expresion'''

def p_comparador(p):
    '''comparador : MAYORQUE
                | MENORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | NOIGUALQUE'''
#*********************ESTRUCTURAS DE DATOS***************************
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
    'pop : VAR VARIABLE IGUAL IZQCHORCHETE lista DERCHORCHETE FINDELINEA'

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
