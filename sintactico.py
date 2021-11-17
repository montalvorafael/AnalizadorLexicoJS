import ply.yacc as yacc
from lexico import tokens
from lexico import lexer

def p_asignacion(p):
    '''asignacion : VAR IGUAL VARIABLE
            | LET IGUAL VARIABLE'''



def p_expresion(p):
    '''expresion : expresion MAS VARIABLE'''


def p_expression_plus(p):
    'expresion : expresion PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expresion : expresion MINUS term'
    p[0] = p[1] - p[3]


def p_expresion_term(p):
    'expresion : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_comparacion(p):
    '''comparacion : expresion comparador term'''

def p_comparador(p):
    '''comparador : MAYORQUE
                | MENOSQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | NOIGUAL'''

# Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
