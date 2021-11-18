import ply.yacc as yacc

from lexico import tokens
#from lexico import lexer

def p_instrucciones(p):
    '''instrucciones : asignacion
                | expresion
                | comparacion
                | arreglo'''

def p_asignacion(p):
    '''asignacion : VAR IGUAL VARIABLE
            | LET IGUAL VARIABLE'''

def p_comparacion(p):
    'comparacion : VARIABLE comparador VARIABLE'

def p_comparador(p):
    '''comparador : MAYORQUE
                | MENORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | NOIGUALQUE'''

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
