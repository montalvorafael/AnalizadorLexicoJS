import ply.yacc as yacc
from lexico import tokens


# =========================================================================================
# Componentes sintácticos.
# =========================================================================================
def p_asignacion_var(p):
    '''asignacion : VAR IGUAL VARIABLE'''
    p[1] = p[3]

def p_asignacion_let(p):
    '''asignacion : LET IGUAL VARIABLE'''
    p[1] = p[3]

def p_expresion(p):
    '''expresion : expresion MAS VARIABLE'''

def p_expresion_mas(p):
    'expresion : expresion MAS term'
    p[0] = p[1] + p[3]

def p_expresion_menos(p):
    'expresion : expresion MENOS term'
    p[0] = p[1] - p[3]

def p_expresion_term(p):
    'expresion : term'
    p[0] = p[1]

def p_term_mult(p):
    'term : term MULT factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : IZQPAREN expresion DERPAREN'
    p[0] = p[2]

def p_comparacion(p):
    '''comparacion : expresion comparador term'''

def p_comparador(p):
    '''comparador : MAYORQUE
    | MENORQUE
    | MAYORIGUALQUE
    | MENORIGUALQUE
    | NOIGUALQUE'''
# =========================================================================================


# =========================================================================================
# Error de sintaxis.
# =========================================================================================
def p_error(p):
    print("Error de sintaxis!")

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

