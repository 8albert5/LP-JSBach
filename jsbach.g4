grammar jsbach;

/* PARSER RULES */

root: defProc* EOF;

defProc: PROCNAME (VAR (VAR)*)? OB cjtInstr CB;

cjtInstr: instr*;
instr: (assign
    | read
    | write
    | play
    | invProc
    | conditional
    | while_
    | addList
    | cutList
    )
    ;

assign: VAR ASSIGN expr;

read: READ VAR;

write: WRITE expr (expr)*;

play: PLAY (VAR | NOTE | LIST);

invProc: PROCNAME (expr (expr)*) ;

conditional: IF exprCond OB cjtInstr CB (ELSE OB cjtInstr CB)?;

while_: WHILE exprCond OB cjtInstr CB;

addList: VAR ADD expr;

cutList: CUT expr;

exprCond: left=expr op=(EQ | NEQ) right=expr    #Cond
        | left=expr op=(LT | LET) right=expr    #Cond
        | left=expr op=(GT | GET) right=expr    #Cond
        ;


expr: left=expr op=(MULT | DIV) right=expr      #InfixOp
    | left=expr op=(PLUS | MINUS) right=expr    #InfixOp
    | left=expr op=MOD right=expr               #InfixOp
    | LP expr RP        #Paren
    | LIST              #List
    | VAR LB VAR RB     #ListElement
    | NOTE              #Note
    | VAR               #Variables
    | NUM               #Numbers
    | STRING            #Strings
    ;

/* LEXER RULES */

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
EQ: '==';
NEQ: '/=';
LT: '<';
LET: '<=';
GT: '>';
GET: '>=';

/* Bracket tokens */
LP: '(';    // Left Parentesis
RP: ')';    // Right Parentesis
LB: '[';    // Left Bracket
RB: ']';    // Right Bracket
LCB: '{';   // Left Curly Bracket
RCB: '}';   // Right Curly Bracket
OB: '|:';   // Open Block
CB: ':|';   // Close Block

PROCNAME: [A-Z][a-zA-Z0-9]*;
NOTE: [A-F]([0-8])?;
VAR: '#'?[a-zA-Z][a-zA-Z0-9]*;
NUM: '-'?[0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
LIST: LCB (NOTE (NOTE)*)? RCB;

/* Handle words that are not keywords */
// IDENTIFIER: [a-zA-Z]+;

COMMENT: '~~~' .*? '~~~' -> skip;
WS: [ \t\r\n]+ -> skip;