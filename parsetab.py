
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'jsleftMASMENOSleftMULTDIVAND ARRAY AWAIT BIGINT BOOLEAN BREAK CASE CATCH CLASS COMA CONST CONSTRUCTOR CONTINUE DEBUGGER DEFAULT DELETE DERCORCHETE DERLLAVE DERPAREN DIV DIVIGUAL DO DOSPUNTOS ELSE EXPORT EXTENDS FINALDELINEA FOR FUNCTION GET IF IGUAL IGUALIGUAL IMPLEMENTS IMPORT INIT INTERFACE IZQCORCHETE IZQLLAVE IZQPAREN LET MAP MAPLOWER MAS MASIGUAL MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOS MENOSIGUAL MODIGUAL MULT MULTIGUAL NEW NOIGUALQUE NULL NUMBER OR PACKAGE POP PRIVATE PROTECTED PUBLIC PUNTO PUSH RETURN SET STRING SUPER SWITCH SYMBOL UNDEFINED VAR VARIABLE VOID WHILEjs : instrucciones\n    | instrucciones jsinstrucciones : declaracion\n    | asignacion\n    | funcion\n    | expresion\n    | comparacion\n    | logica\n    | arreglo\n    | map\n    | if\n    | switch\n    | while\n    | pop\n    | push\n    | mapSetdeclaracion : VAR VARIABLE final_linea\n                | LET VARIABLE final_linea\n                | CONST VARIABLE final_lineadeclaracion : VAR VARIABLE IGUAL tipos_datos final_linea\n                | LET VARIABLE IGUAL tipos_datos final_linea\n                | CONST VARIABLE IGUAL tipos_datos final_linea\n                | VAR VARIABLE IGUAL comparacion final_linea\n                | LET VARIABLE IGUAL comparacion final_linea\n                | CONST VARIABLE IGUAL comparacion final_linea\n                | VAR VARIABLE IGUAL expresion final_linea\n                | LET VARIABLE IGUAL expresion final_linea\n                | CONST VARIABLE IGUAL expresion final_lineaasignacion : VARIABLE operadores_asig tipos_datos final_linea\n    | VARIABLE IGUAL comparacion final_linea\n    | VARIABLE IGUAL expresion final_lineaexpresion : expresion MAS termexpresion : expresion MENOS termcomparacion : expresion operadores_comp termlogica : expresion operadores_log termexpresion : termterm : term MULT factorterm : term DIV factorterm : factorfactor : VARIABLEfactor : tipos_datosfactor : IZQPAREN expresion DERPARENtipos_datos : NUMBER\n    | STRING\n    | BOOLEAN\n    | BIGINT\n    | NULL\n    | SYMBOLoperadores_asig : IGUAL\n    | MASIGUAL\n    | MENOSIGUAL\n    | DIVIGUAL\n    | MODIGUAL\n    | MULTIGUALoperadores_comp : MAYORQUE\n    | MENORQUE\n    | MAYORIGUALQUE\n    | MENORIGUALQUE\n    | NOIGUALQUE\n    | IGUALIGUALoperadores_log : AND\n    | ORfinal_linea : FINALDELINEA\n    | emptyempty :funcion : FUNCTION VARIABLE IZQPAREN VARIABLE DERPAREN IZQLLAVE js DERLLAVEfuncion : FUNCTION VARIABLE IZQPAREN DERPAREN IZQLLAVE js DERLLAVEif : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE\n    | IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ifif : IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVEswitch : SWITCH IZQPAREN VARIABLE DERPAREN IZQLLAVE ncasos DEFAULT DOSPUNTOS js DERLLAVEcasos : CASE tipos_datos DOSPUNTOS asignacion BREAK FINALDELINEA\n    | CASE tipos_datos DOSPUNTOSncasos : casos\n    | casos ncasos\n    while : WHILE IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVEarreglo : VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE FINALDELINEA\n    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN FINALDELINEA\n    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN FINALDELINEA\n    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN FINALDELINEA\n    | VAR VARIABLE IGUAL IZQCORCHETE DERCORCHETE FINALDELINEA\n    | LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE FINALDELINEA\n    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN FINALDELINEA\n    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN FINALDELINEA\n    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN FINALDELINEA\n    | LET VARIABLE IGUAL IZQCORCHETE DERCORCHETE FINALDELINEA\n    | VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE\n    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN\n    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN\n    | VAR VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN\n    | VAR VARIABLE IGUAL IZQCORCHETE DERCORCHETE\n    | LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE\n    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN\n    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN\n    | LET VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN\n    | LET VARIABLE IGUAL IZQCORCHETE DERCORCHETE  lista : lista COMA lista\n    | tipos_datospop : VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN FINALDELINEA\n    | VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPARENpush : VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN FINALDELINEA\n    | VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPARENmap : LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea\n    | VAR VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea\n    | CONST VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_lineamapSet : MAPLOWER PUNTO SET IZQPAREN tipos_datos COMA tipos_datos DERPAREN final_linea'
    
_lr_action_items = {'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,17,17,17,-87,-81,-92,-86,17,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,17,-65,-99,-102,-79,-80,-84,-85,17,-106,-101,-71,-70,]),'LET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,19,19,19,-87,-81,-92,-86,19,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,19,-65,-99,-102,-79,-80,-84,-85,19,-106,-101,-71,-70,]),'CONST':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,20,20,20,-87,-81,-92,-86,20,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,20,-65,-99,-102,-79,-80,-84,-85,20,-106,-101,-71,-70,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,51,57,58,61,62,63,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,199,200,201,202,203,204,205,206,207,211,212,214,216,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,49,-40,57,58,-41,59,61,-36,-43,-39,-44,-45,-46,-47,-48,61,61,61,61,-55,-56,-57,-58,-59,-60,-61,-62,-65,61,-65,-65,-40,61,61,61,89,61,-32,-33,-34,-35,-17,92,-63,-64,-65,-65,-65,-18,61,-19,61,110,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,18,18,18,-87,-81,-92,-86,18,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,18,210,-65,-99,-102,-79,-80,-84,-85,18,-106,-101,-71,-70,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,22,22,22,-87,-81,-92,-86,22,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,22,-65,-99,-102,-79,-80,-84,-85,22,-106,-101,-71,-70,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,26,26,26,-87,-81,-92,-86,26,-77,-88,-65,-82,-93,-65,-65,-67,26,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,26,-65,-99,-102,-79,-80,-84,-85,26,-106,-101,-71,-70,]),'SWITCH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,27,27,27,-87,-81,-92,-86,27,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,27,-65,-99,-102,-79,-80,-84,-85,27,-106,-101,-71,-70,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,28,28,28,-87,-81,-92,-86,28,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,28,-65,-99,-102,-79,-80,-84,-85,28,-106,-101,-71,-70,]),'MAPLOWER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,29,29,29,-87,-81,-92,-86,29,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,29,-65,-99,-102,-79,-80,-84,-85,29,-106,-101,-71,-70,]),'IZQPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,26,27,28,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,51,57,58,59,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,91,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,123,124,125,126,127,129,130,131,132,133,134,135,137,138,140,142,143,144,146,149,150,154,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,23,-36,-43,64,65,66,-39,-44,-45,-46,-47,-48,23,23,23,23,-55,-56,-57,-58,-59,-60,-61,-62,-65,23,-65,-65,83,-40,23,23,23,23,-32,-33,-34,-35,-17,23,-63,-64,-65,-65,-65,-18,23,-19,23,-42,-37,-38,115,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,147,148,-21,-24,-27,-96,151,152,-22,-25,-28,153,23,23,23,162,163,-87,-81,-92,-86,23,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,23,-65,-99,-102,-79,-80,-84,-85,23,-106,-101,-71,-70,]),'NUMBER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,92,93,94,95,96,98,99,100,101,102,103,104,106,107,108,115,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,145,146,147,149,150,151,154,159,161,163,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,25,-36,-43,-39,-44,-45,-46,-47,-48,25,25,25,25,-55,-56,-57,-58,-59,-60,-61,-62,-65,25,25,-50,-51,-52,-53,-54,-65,-65,-40,25,25,25,25,-32,-33,-34,-35,-17,25,-63,-64,-65,-65,-65,-18,25,-19,25,-42,-37,-38,-40,-41,-65,-65,25,-29,-30,-31,-41,-65,-65,25,-41,-65,-65,25,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,25,25,25,-87,25,-81,167,-92,-86,172,25,25,25,25,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,25,-65,-99,-102,-79,-80,-84,-85,25,-106,-101,-71,-70,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,92,93,94,95,96,98,99,100,101,102,103,104,106,107,108,115,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,145,146,147,149,150,151,154,159,161,163,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,31,-36,-43,-39,-44,-45,-46,-47,-48,31,31,31,31,-55,-56,-57,-58,-59,-60,-61,-62,-65,31,31,-50,-51,-52,-53,-54,-65,-65,-40,31,31,31,31,-32,-33,-34,-35,-17,31,-63,-64,-65,-65,-65,-18,31,-19,31,-42,-37,-38,-40,-41,-65,-65,31,-29,-30,-31,-41,-65,-65,31,-41,-65,-65,31,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,31,31,31,-87,31,-81,31,-92,-86,31,31,31,31,31,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,31,-65,-99,-102,-79,-80,-84,-85,31,-106,-101,-71,-70,]),'BOOLEAN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,92,93,94,95,96,98,99,100,101,102,103,104,106,107,108,115,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,145,146,147,149,150,151,154,159,161,163,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,32,-36,-43,-39,-44,-45,-46,-47,-48,32,32,32,32,-55,-56,-57,-58,-59,-60,-61,-62,-65,32,32,-50,-51,-52,-53,-54,-65,-65,-40,32,32,32,32,-32,-33,-34,-35,-17,32,-63,-64,-65,-65,-65,-18,32,-19,32,-42,-37,-38,-40,-41,-65,-65,32,-29,-30,-31,-41,-65,-65,32,-41,-65,-65,32,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,32,32,32,-87,32,-81,32,-92,-86,32,32,32,32,32,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,32,-65,-99,-102,-79,-80,-84,-85,32,-106,-101,-71,-70,]),'BIGINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,92,93,94,95,96,98,99,100,101,102,103,104,106,107,108,115,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,145,146,147,149,150,151,154,159,161,163,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[33,33,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,33,-36,-43,-39,-44,-45,-46,-47,-48,33,33,33,33,-55,-56,-57,-58,-59,-60,-61,-62,-65,33,33,-50,-51,-52,-53,-54,-65,-65,-40,33,33,33,33,-32,-33,-34,-35,-17,33,-63,-64,-65,-65,-65,-18,33,-19,33,-42,-37,-38,-40,-41,-65,-65,33,-29,-30,-31,-41,-65,-65,33,-41,-65,-65,33,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,33,33,33,-87,33,-81,33,-92,-86,33,33,33,33,33,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,33,-65,-99,-102,-79,-80,-84,-85,33,-106,-101,-71,-70,]),'NULL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,92,93,94,95,96,98,99,100,101,102,103,104,106,107,108,115,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,145,146,147,149,150,151,154,159,161,163,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[34,34,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,34,-36,-43,-39,-44,-45,-46,-47,-48,34,34,34,34,-55,-56,-57,-58,-59,-60,-61,-62,-65,34,34,-50,-51,-52,-53,-54,-65,-65,-40,34,34,34,34,-32,-33,-34,-35,-17,34,-63,-64,-65,-65,-65,-18,34,-19,34,-42,-37,-38,-40,-41,-65,-65,34,-29,-30,-31,-41,-65,-65,34,-41,-65,-65,34,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,34,34,34,-87,34,-81,34,-92,-86,34,34,34,34,34,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,34,-65,-99,-102,-79,-80,-84,-85,34,-106,-101,-71,-70,]),'SYMBOL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,23,24,25,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,92,93,94,95,96,98,99,100,101,102,103,104,106,107,108,115,117,118,119,121,125,126,127,129,132,133,134,137,138,140,144,145,146,147,149,150,151,154,159,161,163,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,198,200,201,202,203,204,205,206,207,211,212,214,216,],[35,35,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,35,-36,-43,-39,-44,-45,-46,-47,-48,35,35,35,35,-55,-56,-57,-58,-59,-60,-61,-62,-65,35,35,-50,-51,-52,-53,-54,-65,-65,-40,35,35,35,35,-32,-33,-34,-35,-17,35,-63,-64,-65,-65,-65,-18,35,-19,35,-42,-37,-38,-40,-41,-65,-65,35,-29,-30,-31,-41,-65,-65,35,-41,-65,-65,35,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,35,35,35,-87,35,-81,35,-92,-86,35,35,35,35,35,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,35,-65,-99,-102,-79,-80,-84,-85,35,-106,-101,-71,-70,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,36,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,144,146,149,150,164,166,169,170,171,174,175,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,200,201,202,203,204,205,206,211,212,214,216,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-2,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,-87,-81,-92,-86,-77,-88,-65,-82,-93,-65,-65,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,-65,-99,-102,-79,-80,-84,-85,-106,-101,-71,-70,]),'DERLLAVE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,24,25,30,31,32,33,34,35,36,49,57,58,61,68,69,70,71,72,74,75,76,77,78,79,81,84,85,86,92,93,94,95,98,99,100,101,102,103,106,107,108,117,118,119,121,125,126,127,129,132,133,134,144,146,149,150,155,156,160,164,166,169,170,171,174,175,176,177,178,182,184,186,187,188,189,190,191,192,193,194,195,196,200,201,202,203,204,205,206,208,211,212,213,214,216,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-2,-65,-65,-65,-40,-32,-33,-34,-35,-17,-63,-64,-65,-65,-65,-18,-19,-42,-37,-38,-40,-41,-65,-65,-29,-30,-31,-41,-65,-65,-41,-65,-65,-20,-23,-26,-91,-21,-24,-27,-96,-22,-25,-28,-87,-81,-92,-86,177,178,182,-77,-88,-65,-82,-93,-65,-65,195,-67,-68,-76,-100,-78,-89,-90,-104,-83,-94,-95,-103,-105,-66,-69,-65,-99,-102,-79,-80,-84,-85,214,-106,-101,216,-71,-70,]),'MAS':([6,18,21,24,25,30,31,32,33,34,35,60,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[37,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,37,-40,-32,-33,37,-42,-37,-38,37,-40,-41,37,-41,37,-41,37,]),'MENOS':([6,18,21,24,25,30,31,32,33,34,35,60,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[38,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,38,-40,-32,-33,38,-42,-37,-38,38,-40,-41,38,-41,38,-41,38,]),'MAYORQUE':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[41,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,41,-42,-37,-38,41,-40,-41,41,-41,41,-41,41,]),'MENORQUE':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[42,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,42,-42,-37,-38,42,-40,-41,42,-41,42,-41,42,]),'MAYORIGUALQUE':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[43,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,43,-42,-37,-38,43,-40,-41,43,-41,43,-41,43,]),'MENORIGUALQUE':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[44,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,44,-42,-37,-38,44,-40,-41,44,-41,44,-41,44,]),'NOIGUALQUE':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[45,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,45,-42,-37,-38,45,-40,-41,45,-41,45,-41,45,]),'IGUALIGUAL':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,78,84,85,86,88,92,93,95,101,103,106,108,],[46,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,46,-42,-37,-38,46,-40,-41,46,-41,46,-41,46,]),'AND':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,84,85,86,],[47,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,-42,-37,-38,]),'OR':([6,18,21,24,25,30,31,32,33,34,35,61,68,69,84,85,86,],[48,-40,-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,-42,-37,-38,]),'IGUAL':([18,49,57,58,210,],[51,73,80,82,51,]),'MULT':([18,21,24,25,30,31,32,33,34,35,61,68,69,70,71,84,85,86,92,93,101,106,],[-40,-41,62,-43,-39,-44,-45,-46,-47,-48,-40,62,62,62,62,-42,-37,-38,-40,-41,-41,-41,]),'DIV':([18,21,24,25,30,31,32,33,34,35,61,68,69,70,71,84,85,86,92,93,101,106,],[-40,-41,63,-43,-39,-44,-45,-46,-47,-48,-40,63,63,63,63,-42,-37,-38,-40,-41,-41,-41,]),'MASIGUAL':([18,210,],[52,52,]),'MENOSIGUAL':([18,210,],[53,53,]),'DIVIGUAL':([18,210,],[54,54,]),'MODIGUAL':([18,210,],[55,55,]),'MULTIGUAL':([18,210,],[56,56,]),'DERPAREN':([21,24,25,30,31,32,33,34,35,60,61,68,69,70,83,84,85,86,87,89,90,110,122,147,148,151,152,153,162,165,167,168,172,173,183,185,],[-41,-36,-43,-39,-44,-45,-46,-47,-48,84,-40,-32,-33,-34,111,-42,-37,-38,112,113,114,136,-98,166,169,171,174,175,184,-97,187,188,191,192,200,202,]),'FINALDELINEA':([21,24,25,30,31,32,33,34,35,49,57,58,61,68,69,70,76,77,78,84,85,86,92,93,94,95,101,102,103,106,107,108,121,129,144,149,166,169,171,174,175,184,187,188,191,192,200,202,215,],[-41,-36,-43,-39,-44,-45,-46,-47,-48,74,74,74,-40,-32,-33,-34,74,74,74,-42,-37,-38,-40,74,74,74,74,74,74,74,74,74,146,150,164,170,186,74,190,74,74,201,203,204,205,206,74,212,217,]),'BREAK':([21,24,25,30,31,32,33,34,35,61,68,69,70,74,75,76,77,78,84,85,86,98,99,100,209,],[-41,-36,-43,-39,-44,-45,-46,-47,-48,-40,-32,-33,-34,-63,-64,-65,-65,-65,-42,-37,-38,-29,-30,-31,215,]),'DERCORCHETE':([25,31,32,33,34,35,96,104,120,122,128,165,],[-43,-44,-45,-46,-47,-48,121,129,144,-98,149,-97,]),'COMA':([25,31,32,33,34,35,120,122,128,141,165,167,168,172,173,185,],[-43,-44,-45,-46,-47,-48,145,-98,145,161,145,-43,145,-43,145,145,]),'DOSPUNTOS':([25,31,32,33,34,35,179,181,],[-43,-44,-45,-46,-47,-48,198,199,]),'PUNTO':([29,92,],[67,116,]),'SET':([67,],[91,]),'IZQCORCHETE':([73,80,],[96,104,]),'NEW':([73,80,82,],[97,105,109,]),'ARRAY':([97,105,],[123,130,]),'MAP':([97,105,109,],[124,131,135,]),'IZQLLAVE':([111,112,113,114,136,197,],[137,138,139,140,154,207,]),'POP':([116,],[142,]),'PUSH':([116,],[143,]),'CASE':([139,158,199,217,],[159,159,-73,-72,]),'DEFAULT':([157,158,180,199,217,],[179,-74,-75,-73,-72,]),'ELSE':([178,],[197,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'js':([0,2,137,138,140,154,198,207,],[1,36,155,156,160,176,208,213,]),'instrucciones':([0,2,137,138,140,154,198,207,],[2,2,2,2,2,2,2,2,]),'declaracion':([0,2,137,138,140,154,198,207,],[3,3,3,3,3,3,3,3,]),'asignacion':([0,2,137,138,140,154,198,199,207,],[4,4,4,4,4,4,4,209,4,]),'funcion':([0,2,137,138,140,154,198,207,],[5,5,5,5,5,5,5,5,]),'expresion':([0,2,23,51,64,66,73,80,82,137,138,140,154,198,207,],[6,6,60,78,88,88,95,103,108,6,6,6,6,6,6,]),'comparacion':([0,2,51,64,66,73,80,82,137,138,140,154,198,207,],[7,7,77,87,90,94,102,107,7,7,7,7,7,7,]),'logica':([0,2,137,138,140,154,198,207,],[8,8,8,8,8,8,8,8,]),'arreglo':([0,2,137,138,140,154,198,207,],[9,9,9,9,9,9,9,9,]),'map':([0,2,137,138,140,154,198,207,],[10,10,10,10,10,10,10,10,]),'if':([0,2,137,138,140,154,178,198,207,],[11,11,11,11,11,11,196,11,11,]),'switch':([0,2,137,138,140,154,198,207,],[12,12,12,12,12,12,12,12,]),'while':([0,2,137,138,140,154,198,207,],[13,13,13,13,13,13,13,13,]),'pop':([0,2,137,138,140,154,198,207,],[14,14,14,14,14,14,14,14,]),'push':([0,2,137,138,140,154,198,207,],[15,15,15,15,15,15,15,15,]),'mapSet':([0,2,137,138,140,154,198,207,],[16,16,16,16,16,16,16,16,]),'tipos_datos':([0,2,23,37,38,39,40,50,51,62,63,64,66,73,80,82,96,104,115,137,138,140,145,147,151,154,159,161,163,198,207,],[21,21,21,21,21,21,21,76,21,21,21,21,21,93,101,106,122,122,141,21,21,21,122,122,122,21,181,183,122,21,21,]),'term':([0,2,23,37,38,39,40,51,64,66,73,80,82,137,138,140,154,198,207,],[24,24,24,68,69,70,71,24,24,24,24,24,24,24,24,24,24,24,24,]),'factor':([0,2,23,37,38,39,40,51,62,63,64,66,73,80,82,137,138,140,154,198,207,],[30,30,30,30,30,30,30,30,85,86,30,30,30,30,30,30,30,30,30,30,30,]),'operadores_comp':([6,78,88,95,103,108,],[39,39,39,39,39,39,]),'operadores_log':([6,],[40,]),'operadores_asig':([18,210,],[50,50,]),'final_linea':([49,57,58,76,77,78,93,94,95,101,102,103,106,107,108,169,174,175,200,],[72,79,81,98,99,100,117,118,119,125,126,127,132,133,134,189,193,194,211,]),'empty':([49,57,58,76,77,78,93,94,95,101,102,103,106,107,108,169,174,175,200,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'lista':([96,104,145,147,151,163,],[120,128,165,168,173,185,]),'ncasos':([139,158,],[157,180,]),'casos':([139,158,],[158,158,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> js","S'",1,None,None,None),
  ('js -> instrucciones','js',1,'p_js','sintactico.py',16),
  ('js -> instrucciones js','js',2,'p_js','sintactico.py',17),
  ('instrucciones -> declaracion','instrucciones',1,'p_instrucciones','sintactico.py',20),
  ('instrucciones -> asignacion','instrucciones',1,'p_instrucciones','sintactico.py',21),
  ('instrucciones -> funcion','instrucciones',1,'p_instrucciones','sintactico.py',22),
  ('instrucciones -> expresion','instrucciones',1,'p_instrucciones','sintactico.py',23),
  ('instrucciones -> comparacion','instrucciones',1,'p_instrucciones','sintactico.py',24),
  ('instrucciones -> logica','instrucciones',1,'p_instrucciones','sintactico.py',25),
  ('instrucciones -> arreglo','instrucciones',1,'p_instrucciones','sintactico.py',26),
  ('instrucciones -> map','instrucciones',1,'p_instrucciones','sintactico.py',27),
  ('instrucciones -> if','instrucciones',1,'p_instrucciones','sintactico.py',28),
  ('instrucciones -> switch','instrucciones',1,'p_instrucciones','sintactico.py',29),
  ('instrucciones -> while','instrucciones',1,'p_instrucciones','sintactico.py',30),
  ('instrucciones -> pop','instrucciones',1,'p_instrucciones','sintactico.py',31),
  ('instrucciones -> push','instrucciones',1,'p_instrucciones','sintactico.py',32),
  ('instrucciones -> mapSet','instrucciones',1,'p_instrucciones','sintactico.py',33),
  ('declaracion -> VAR VARIABLE final_linea','declaracion',3,'p_declaracion_SinAsig','sintactico.py',37),
  ('declaracion -> LET VARIABLE final_linea','declaracion',3,'p_declaracion_SinAsig','sintactico.py',38),
  ('declaracion -> CONST VARIABLE final_linea','declaracion',3,'p_declaracion_SinAsig','sintactico.py',39),
  ('declaracion -> VAR VARIABLE IGUAL tipos_datos final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',42),
  ('declaracion -> LET VARIABLE IGUAL tipos_datos final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',43),
  ('declaracion -> CONST VARIABLE IGUAL tipos_datos final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',44),
  ('declaracion -> VAR VARIABLE IGUAL comparacion final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',45),
  ('declaracion -> LET VARIABLE IGUAL comparacion final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',46),
  ('declaracion -> CONST VARIABLE IGUAL comparacion final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',47),
  ('declaracion -> VAR VARIABLE IGUAL expresion final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',48),
  ('declaracion -> LET VARIABLE IGUAL expresion final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',49),
  ('declaracion -> CONST VARIABLE IGUAL expresion final_linea','declaracion',5,'p_declaracion_ConAsig','sintactico.py',50),
  ('asignacion -> VARIABLE operadores_asig tipos_datos final_linea','asignacion',4,'p_asignacion','sintactico.py',54),
  ('asignacion -> VARIABLE IGUAL comparacion final_linea','asignacion',4,'p_asignacion','sintactico.py',55),
  ('asignacion -> VARIABLE IGUAL expresion final_linea','asignacion',4,'p_asignacion','sintactico.py',56),
  ('expresion -> expresion MAS term','expresion',3,'p_expresion_mas','sintactico.py',60),
  ('expresion -> expresion MENOS term','expresion',3,'p_expresion_menos','sintactico.py',64),
  ('comparacion -> expresion operadores_comp term','comparacion',3,'p_expresion_comp','sintactico.py',68),
  ('logica -> expresion operadores_log term','logica',3,'p_expresion_log','sintactico.py',71),
  ('expresion -> term','expresion',1,'p_expresion_term','sintactico.py',74),
  ('term -> term MULT factor','term',3,'p_term_mult','sintactico.py',79),
  ('term -> term DIV factor','term',3,'p_term_div','sintactico.py',83),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',87),
  ('factor -> VARIABLE','factor',1,'p_factor_var','sintactico.py',92),
  ('factor -> tipos_datos','factor',1,'p_factor_num','sintactico.py',95),
  ('factor -> IZQPAREN expresion DERPAREN','factor',3,'p_factor_expr','sintactico.py',98),
  ('tipos_datos -> NUMBER','tipos_datos',1,'p_tipos_datos','sintactico.py',102),
  ('tipos_datos -> STRING','tipos_datos',1,'p_tipos_datos','sintactico.py',103),
  ('tipos_datos -> BOOLEAN','tipos_datos',1,'p_tipos_datos','sintactico.py',104),
  ('tipos_datos -> BIGINT','tipos_datos',1,'p_tipos_datos','sintactico.py',105),
  ('tipos_datos -> NULL','tipos_datos',1,'p_tipos_datos','sintactico.py',106),
  ('tipos_datos -> SYMBOL','tipos_datos',1,'p_tipos_datos','sintactico.py',107),
  ('operadores_asig -> IGUAL','operadores_asig',1,'p_operadores_asig','sintactico.py',110),
  ('operadores_asig -> MASIGUAL','operadores_asig',1,'p_operadores_asig','sintactico.py',111),
  ('operadores_asig -> MENOSIGUAL','operadores_asig',1,'p_operadores_asig','sintactico.py',112),
  ('operadores_asig -> DIVIGUAL','operadores_asig',1,'p_operadores_asig','sintactico.py',113),
  ('operadores_asig -> MODIGUAL','operadores_asig',1,'p_operadores_asig','sintactico.py',114),
  ('operadores_asig -> MULTIGUAL','operadores_asig',1,'p_operadores_asig','sintactico.py',115),
  ('operadores_comp -> MAYORQUE','operadores_comp',1,'p_operadores_comp','sintactico.py',118),
  ('operadores_comp -> MENORQUE','operadores_comp',1,'p_operadores_comp','sintactico.py',119),
  ('operadores_comp -> MAYORIGUALQUE','operadores_comp',1,'p_operadores_comp','sintactico.py',120),
  ('operadores_comp -> MENORIGUALQUE','operadores_comp',1,'p_operadores_comp','sintactico.py',121),
  ('operadores_comp -> NOIGUALQUE','operadores_comp',1,'p_operadores_comp','sintactico.py',122),
  ('operadores_comp -> IGUALIGUAL','operadores_comp',1,'p_operadores_comp','sintactico.py',123),
  ('operadores_log -> AND','operadores_log',1,'p_operadores_log','sintactico.py',126),
  ('operadores_log -> OR','operadores_log',1,'p_operadores_log','sintactico.py',127),
  ('final_linea -> FINALDELINEA','final_linea',1,'p_final_linea','sintactico.py',130),
  ('final_linea -> empty','final_linea',1,'p_final_linea','sintactico.py',131),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',134),
  ('funcion -> FUNCTION VARIABLE IZQPAREN VARIABLE DERPAREN IZQLLAVE js DERLLAVE','funcion',8,'p_funcion_unparametro','sintactico.py',145),
  ('funcion -> FUNCTION VARIABLE IZQPAREN DERPAREN IZQLLAVE js DERLLAVE','funcion',7,'p_funcion_sinparametro','sintactico.py',150),
  ('if -> IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE','if',7,'p_if','sintactico.py',160),
  ('if -> IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE if','if',8,'p_if','sintactico.py',161),
  ('if -> IF IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE ELSE IZQLLAVE js DERLLAVE','if',11,'p_if_else','sintactico.py',164),
  ('switch -> SWITCH IZQPAREN VARIABLE DERPAREN IZQLLAVE ncasos DEFAULT DOSPUNTOS js DERLLAVE','switch',10,'p_switch','sintactico.py',171),
  ('casos -> CASE tipos_datos DOSPUNTOS asignacion BREAK FINALDELINEA','casos',6,'p_casos','sintactico.py',174),
  ('casos -> CASE tipos_datos DOSPUNTOS','casos',3,'p_casos','sintactico.py',175),
  ('ncasos -> casos','ncasos',1,'p_ncasos','sintactico.py',178),
  ('ncasos -> casos ncasos','ncasos',2,'p_ncasos','sintactico.py',179),
  ('while -> WHILE IZQPAREN comparacion DERPAREN IZQLLAVE js DERLLAVE','while',7,'p_while','sintactico.py',185),
  ('arreglo -> VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE FINALDELINEA','arreglo',7,'p_arreglo','sintactico.py',195),
  ('arreglo -> VAR VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN FINALDELINEA','arreglo',8,'p_arreglo','sintactico.py',196),
  ('arreglo -> VAR VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN FINALDELINEA','arreglo',9,'p_arreglo','sintactico.py',197),
  ('arreglo -> VAR VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN FINALDELINEA','arreglo',9,'p_arreglo','sintactico.py',198),
  ('arreglo -> VAR VARIABLE IGUAL IZQCORCHETE DERCORCHETE FINALDELINEA','arreglo',6,'p_arreglo','sintactico.py',199),
  ('arreglo -> LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE FINALDELINEA','arreglo',7,'p_arreglo','sintactico.py',200),
  ('arreglo -> LET VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN FINALDELINEA','arreglo',8,'p_arreglo','sintactico.py',201),
  ('arreglo -> LET VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN FINALDELINEA','arreglo',9,'p_arreglo','sintactico.py',202),
  ('arreglo -> LET VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN FINALDELINEA','arreglo',9,'p_arreglo','sintactico.py',203),
  ('arreglo -> LET VARIABLE IGUAL IZQCORCHETE DERCORCHETE FINALDELINEA','arreglo',6,'p_arreglo','sintactico.py',204),
  ('arreglo -> VAR VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE','arreglo',6,'p_arreglo','sintactico.py',205),
  ('arreglo -> VAR VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN','arreglo',7,'p_arreglo','sintactico.py',206),
  ('arreglo -> VAR VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN','arreglo',8,'p_arreglo','sintactico.py',207),
  ('arreglo -> VAR VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN','arreglo',8,'p_arreglo','sintactico.py',208),
  ('arreglo -> VAR VARIABLE IGUAL IZQCORCHETE DERCORCHETE','arreglo',5,'p_arreglo','sintactico.py',209),
  ('arreglo -> LET VARIABLE IGUAL IZQCORCHETE lista DERCORCHETE','arreglo',6,'p_arreglo','sintactico.py',210),
  ('arreglo -> LET VARIABLE IGUAL NEW ARRAY IZQPAREN DERPAREN','arreglo',7,'p_arreglo','sintactico.py',211),
  ('arreglo -> LET VARIABLE IGUAL NEW ARRAY IZQPAREN NUMBER DERPAREN','arreglo',8,'p_arreglo','sintactico.py',212),
  ('arreglo -> LET VARIABLE IGUAL NEW ARRAY IZQPAREN lista DERPAREN','arreglo',8,'p_arreglo','sintactico.py',213),
  ('arreglo -> LET VARIABLE IGUAL IZQCORCHETE DERCORCHETE','arreglo',5,'p_arreglo','sintactico.py',214),
  ('lista -> lista COMA lista','lista',3,'p_lista','sintactico.py',223),
  ('lista -> tipos_datos','lista',1,'p_lista','sintactico.py',224),
  ('pop -> VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN FINALDELINEA','pop',9,'p_pop','sintactico.py',228),
  ('pop -> VAR VARIABLE IGUAL VARIABLE PUNTO POP IZQPAREN DERPAREN','pop',8,'p_pop','sintactico.py',229),
  ('push -> VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN FINALDELINEA','push',10,'p_push','sintactico.py',233),
  ('push -> VAR VARIABLE IGUAL VARIABLE PUNTO PUSH IZQPAREN lista DERPAREN','push',9,'p_push','sintactico.py',234),
  ('map -> LET VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea','map',8,'p_map','sintactico.py',240),
  ('map -> VAR VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea','map',8,'p_map','sintactico.py',241),
  ('map -> CONST VARIABLE IGUAL NEW MAP IZQPAREN DERPAREN final_linea','map',8,'p_map','sintactico.py',242),
  ('mapSet -> MAPLOWER PUNTO SET IZQPAREN tipos_datos COMA tipos_datos DERPAREN final_linea','mapSet',9,'p_mapSet','sintactico.py',249),
]
