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

play: PLAY expr;

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
    | LP expr RP                                #Paren
    | LCB (expr (expr)* )? RCB                  #List
    | VAR LB VAR RB                             #ListElement
    | NOTE                                      #Note
    | VAR                                       #Variables
    | NUM                                       #Numbers
    | STRING                                    #Strings
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

VAR: '#'?[a-z][a-zA-Z0-9]*;
NUM: '-'?[0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"';
NOTE: ([A-B]([0-8])? | [C-G]([1-8])?);
PROCNAME: [A-Z][a-zA-Z0-9]*;

COMMENT: '~~~' .*? '~~~' -> skip;
WS: [ \t\r\n]+ -> skip;