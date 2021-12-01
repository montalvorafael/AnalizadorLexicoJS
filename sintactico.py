import ply.yacc as yacc
from lexico import tokens
from lexico import lexer_js

# =========================================================================================
# Básico.
# =========================================================================================
#Rafael Montalvo : Switch, funcion sin parametros, mapa ( metodos set y get ), semantica de operaciones
#Willy Mateo: While, funcion con retorno, set ( metodos add y has), semantica metodos de las estructuras.
#Margarita Mawyin : if, funciones con parametros, array ( metodos pop y push), semantica de condicionales
resultado_gramatica = []
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
    | expresion final_linea
    | comparacion
    | logica
    | if
    | switch
    | while
    | funcion
    | reglasemanticaop final_linea
    | print_encabezado final_linea
    '''

# Declaración =============================================================================
def p_declaracion_SinAsig(p):
    '''declaracion : VAR VARIABLE
    | LET VARIABLE
    | CONST VARIABLE
    '''

def p_declaracion_ConAsig(p):
    '''declaracion : VAR VARIABLE IGUAL comparacion
    | LET VARIABLE IGUAL comparacion
    | CONST VARIABLE IGUAL comparacion
    | VAR VARIABLE IGUAL reglasemanticaop
    | LET VARIABLE IGUAL reglasemanticaop
    | CONST VARIABLE IGUAL reglasemanticaop
    | VAR VARIABLE IGUAL expresion
    | LET VARIABLE IGUAL expresion
    | CONST VARIABLE IGUAL expresion
    '''

# Asignación ==============================================================================
def p_asignacion(p):
    '''asignacion : VARIABLE operadores_asig tipos_datos
    | VARIABLE operadores_asig VARIABLE
    | VARIABLE IGUAL comparacion
    | VARIABLE IGUAL expresion
    | VARIABLE IGUAL reglasemanticaop
    | arreglo_slicing IGUAL tipos_datos
    '''

# Expresión ===============================================================================
def p_expresion_comp(p):
   'comparacion : expresion operadores_comp term'

def p_expresion_log(p):
    '''logica : comparacion operadores_log term
                | comparacion operadores_log expresion
                | comparacion operadores_log comparacion
                | comparacion operadores_log logica'''

def p_expresion_term(p):
    'expresion : term'
    # p[0] = p[1]

def p_print_encabezado(p):
    '''print_encabezado : CONSOLE PUNTO LOG IZQPAREN print_linea DERPAREN
    | CONSOLE PUNTO LOG IZQPAREN switchdatos DERPAREN'''

def p_print_linea(p):
    '''print_linea : STRING COMA VARIABLE
        | STRING COMA VARIABLE COMA print_linea'''


# Return.
def p_expresion_return(p):
    '''expresion : RETURN expresion'''

# Termino =================================================================================
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

# Agrupaciones de datos y operadores ======================================================
def p_tipos_datos(p):
    '''tipos_datos : NUMBER
    | STRING
    | BOOLEAN
    | BIGINT
    | NULL
    | SYMBOL
    | estructuras_datos'''

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
def p_if_semantica(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
    | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE if
    | IF IZQPAREN logica DERPAREN IZQLLAVE js DERLLAVE
    | IF IZQPAREN logica DERPAREN IZQLLAVE js DERLLAVE if'''

def p_if_else_semantica(p):
    '''if : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE
            | IF IZQPAREN logica DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE'''

# Switch ==================================================================================
def p_switch_semantica(p):
    '''switch : SWITCH IZQPAREN switchdatos DERPAREN IZQLLAVE ncasos DEFAULT DOSPUNTOS js DERLLAVE'''

def p_ncasos(p):
    '''ncasos : casos
    | casos ncasos
    '''

def p_casos(p):
    '''casos : CASE switchdatos DOSPUNTOS js BREAK final_linea
    | CASE switchdatos DOSPUNTOS'''
def p_switchdatos(p):
    '''switchdatos : NUMBER
    | STRING
    | BOOLEAN
    | BIGINT
    | VARIABLE'''
# While ===================================================================================
def p_while_semantica(p):
    '''while : WHILE IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE
            | WHILE IZQPAREN logica DERPAREN IZQLLAVE js DERLLAVE'''

# =========================================================================================
#Regla semantica para los condicionales lista - M. Mawyin


# =========================================================================================
# Estructuras de datos.
# =========================================================================================
def p_estructuras_datos(p):
    '''estructuras_datos : arreglo
    | map
    | set
    | estructuras_datos_metod
    '''
def p_estructuras_datos_metod(p):
    '''estructuras_datos_metod : arreglo_metodos
    | map_metodos
    | set_metodos
    '''

# Array ===================================================================================
def p_arreglo(p):
    '''arreglo : IZQCORCHETE lista DERCORCHETE
    | IZQCORCHETE DERCORCHETE
    | NEW ARRAY IZQPAREN DERPAREN
    | NEW ARRAY IZQPAREN lista DERPAREN
    '''

def p_lista(p):
    '''lista : lista_elemento
    | lista_elemento COMA lista
    | empty'''

def p_lista_elemento(p):
    '''lista_elemento : tipos_datos
    | VARIABLE'''

# Métodos.
def p_pop(p):
    '''arreglo_metodos : VARIABLE POP_METODO IZQPAREN DERPAREN'''

def p_push(p):
    '''arreglo_metodos : VARIABLE PUSH_METODO IZQPAREN lista DERPAREN'''

def p_arregloSlicing(p):
    'arreglo_slicing : VARIABLE IZQCORCHETE NUMBER DERCORCHETE'

# Map =====================================================================================
def p_map(p):
    '''map : NEW MAP IZQPAREN DERPAREN final_linea
    '''

# Métodos.
def p_map_set(p):
    '''map_metodos : VARIABLE SET_METODO IZQPAREN switchdatos COMA switchdatos DERPAREN final_linea'''

def p_map_get(p):
    'map_metodos : VARIABLE GET_METODO IZQPAREN switchdatos DERPAREN final_linea'

# Set =====================================================================================
def p_set(p):
    '''set : NEW SET_ESTRUC IZQPAREN DERPAREN
    | NEW SET_ESTRUC IZQPAREN NULL DERPAREN
    | NEW SET_ESTRUC IZQPAREN lista DERPAREN
    '''

# Métodos.
def p_set_add(p):
    '''set_metodos : VARIABLE ADD_METODO IZQPAREN lista_elemento DERPAREN'''

def p_set_has(p):
    '''set_metodos : VARIABLE HAS_METODO IZQPAREN lista_elemento DERPAREN'''
# =========================================================================================


# =========================================================================================
# Error sintáctico.
# =========================================================================================
def p_error(p):
    error = "Error de sintaxis."
    print(error)

    global resultado_gramatica
    if p:
        resultado = "Error de tipo {} en el valor {}".format(str(p.type), str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico"
        print(resultado)
    resultado_gramatica.append(resultado)
# =========================================================================================

# regla semantica operaciones
def p_valoroperaciones(p):
    '''valoroperaciones : NUMBER
    | BIGINT
    | VARIABLE'''

def p_reglasemanticaop_mas(p):
    '''reglasemanticaop : valoroperaciones MAS valoroperaciones
    | valoroperaciones MAS reglasemanticaop'''
    # p[0] = p[1] + p[3]

def p_reglasemanticaop_menos(p):
    '''reglasemanticaop : valoroperaciones MENOS valoroperaciones
    | valoroperaciones MENOS reglasemanticaop'''
    # p[0] = p[1] - p[3]
def p_reglasemanticaop_mult(p):
    '''reglasemanticaop : valoroperaciones MULT valoroperaciones
    | valoroperaciones MULT reglasemanticaop'''
    # p[0] = p[1] * p[3]

def p_reglasemanticaop_div(p):
    '''reglasemanticaop : valoroperaciones DIV valoroperaciones
    | valoroperaciones DIV reglasemanticaop'''
    # p[0] = p[1] / p[3]
def p_reglasemanticaop_mod(p):
    '''reglasemanticaop : valoroperaciones MODULO valoroperaciones
    | valoroperaciones MODULO reglasemanticaop'''

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
    'var num;',
    'var NULL;',
    'num2 = true',
    '10/"hola"', #error semantico
    'num = num-num3',
    'num=100',
    '5*2/1+1',
    '1*1+1',
    '4+5+5-true',
    '4+5+5+"ok"',
    'var _nueva = 0xfff;',
    'var pruebaE = 23e-8;',
    'var NuevaVariable = true;',
    'var $_$0 = "grupo 8";',
    'var sym1 = Symbol();',
    'var sym2 = Symbol("foo");',
    'let t1posdat0s = 789.8;',
    'let $otranueva = false;',
    'let pruebasNega = -789n;',

    # Operadores logicos.
    'n>0 && n <5',
    'num>5 || num ==10',
    'num>5 || num ==10 || num <= 0',
    'num>5 || num ==10 && num <= 0',
    'num>5 || num && 10', # error semantico

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
    'map.get("clave")',
    'map.get(1);',
    'let newSet = new Set()',
    'let newSet = new Set(null)',
    'let newSet = new Set("Ana","Diana","Tom")',
    'mySet.has(Math);',
    'mySet.has("Hola MUNDO");',
    'mySet.has(7);',
    'mySet.has(5.45);',
    'mySet.add("hola mundo");',
    'mySet.add(5.45);',
    'mySet.add(3);',

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
    if (num2 > num || num2 == 10) {
            num2=num2-num
        } if (num > num3) {
            num =num-num3
        } else {
            num=100
        }
    ''',
    '''
    while (n < 3 ) {
        x = n;
    }
    ''',
    '''
    while (n < 3 && n>0) {
        x = n;
    }
    ''',
    '''
    while (menor <= 3) {
        x = n;
        let s = new Array();
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
        let sopa de letras= "fndklañfdiafhwbnlewq"
        numero* numero;
    }
    ''',
    '''
    function presentacion(nombre){
         console.log("Mi nombres es" , nombre );
    }
    ''',
    '''
    function presentacionCompleta(nombre,apellido){
        console.log("Mi nombres es" , nombre ," y mi apelldio es " , apellido);
    }
    ''',
    '''
    function newFunction(a, b, c) {
        let suma = a + b + c;
        return 0;
    }
    '''
]

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser_js.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

for instruccion in data:
    print(instruccion)
    result = parser_js.parse(instruccion, lexer= lexer_js)
    print(result)
    print()

# =========================================================================================

