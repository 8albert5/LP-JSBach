grammar jsbach;
root: defProc* EOF;

defProc: PROCNAME (VAR (VAR)*)? OB cjtInstr CB;

cjtInstr: instr*;
instr: (assign
    | read
    | write
    | play
    | invProc
    | cond
    | while_
    /*
    | addList
    | cutList
     */
    )
    ;

assign: VAR ASSIGN expr;

read: READ VAR;

write: WRITE expr (expr)*;

play: PLAY expr;

invProc: PROCNAME (expr (expr)*)? ;

cond: IF exprCond OB cjtInstr CB (ELSE OB cjtInstr CB);

while_: WHILE exprCond OB cjtInstr CB;

addList: ADD expr;

cutList: CUT expr;

exprCond: expr EQ expr  #Equal
    | expr NEQ expr     #NotEqual
    | expr LT expr      #LessThan
    | expr LET expr     #LessEqThan
    | expr GT expr      #GrThan
    | expr GET expr     #GrEqThan
    ;



expr: expr MULT expr    #Multiplicacio
    | expr DIV expr     #Divisio
    | expr MOD expr     #Modul
    | expr PLUS expr    #Suma
    | expr MINUS expr   #Resta
    | LP expr RP        #Parentesis
    | LB (expr)* RB     #Llistes
    | VAR               #Variables
    | NUM               #Numeros
    | STRING            #Strings
    ;

/* Instruccions de JSBach */
ASSIGN: '<-';
READ: '<?>';
WRITE: '<!>';
PLAY: '<:>';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
ADD: '<<';
CUT: '8<';

/* Operadors aritmètics */
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';

/* Operadors relacionals */
EQ: '=';
NEQ: '/=';
LT: '<';
LET: '<=';
GT: '>';
GET: '>=';

/* Altres tokens */
LP: '(';
RP: ')';
LB: '{';
RB: '}';
OB: '|:'; // Open Block
CB: ':|'; // Close Block


PROCNAME: [A-Z][a-zA-Z0-9]*;
VAR: [a-zA-Z][a-zA-Z0-9]*;
NUM: '-'?[0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';

/* Handle words that are not keywords */
IDENTIFIER: [a-zA-Z]+;

COMMENT: '~~~' .*? '~~~' -> skip;
WS: [ \t\r\n]+ -> channel(HIDDEN);