# Generated from jsbach.g4 by ANTLR 4.7.2
if __name__ is not None and "." in __name__:
    from jsbachVisitor import jsbachVisitor
else:
    from jsbachVisitor import jsbachVisitor


# Aquesta classe defineix els errors més comuns de JSBach
class JSBachError(Exception):
    def __init__(self, msg):
        self.message = f"JSBachError: {msg}"


class Procediment(object):
    def __init__(self, name, params, instructions):
        self.name = name
        self.params = params
        self.instructions = instructions


class JSBachTreeVisitor(jsbachVisitor):
    notes = {
        # "A": 28,    "B": 29,    "C": 23,    "D": 24,    "E": 25,    "F": 26,    "G": 27,
        "A0": 0,    "B0": 1,    "C1": 2,	"D1": 3,	"E1": 4,	"F1": 5,	"G1": 6,
        "A1": 7,    "B1": 8,    "C2": 9,	"D2": 10,	"E2": 11,	"F2": 12,	"G2": 13,
        "A2": 14,   "B2": 15,   "C3": 16,	"D3": 17,	"E3": 18,	"F3": 19,	"G3": 20,
        "A3": 21,   "B3": 22,   "C4": 23,	"D4": 24,	"E4": 25,	"F4": 26,	"G4": 27,
        "A4": 28,   "B4": 29,   "C5": 30,	"D5": 31,	"E5": 32,	"F5": 33,	"G5": 34,
        "A5": 35,   "B5": 36,   "C6": 37,	"D6": 38,	"E6": 39,	"F6": 40,	"G6": 41,
        "A6": 42,   "B6": 43,   "C7": 44,	"D7": 45,	"E7": 46,	"F7": 47,	"G7": 48,
        "A7": 49,   "B7": 50,   "C8": 51,
        "A8": 52,   "B8": 53,
    }

    def __init__(self, entry="Main", params=[]):
        self.entry = entry
        self.params = params

        self.var_scope_stack = []
        self.procediments = {}
        self.music_sheet = []

    def executeProc(self, name, params):
        procediment = self.procediments[name]
        expected_params = len(procediment.params)

        # Comprovem si el procediment té el número de paràmetres correcte.
        if expected_params != len(params):
            raise JSBachError(
                f"Procediment \"{name}\" espera {expected_params} paràmetres i n'ha rebut {len(params)}.")

        # Creem el diccionari de variable -> valor
        variables = {}
        for var_name, value in zip(procediment.params, params):
            variables[var_name] = value

        # Afegim nou scope de variables a la pila
        self.var_scope_stack.append(variables)
        # L'execució fa servir l'element de la pila
        self.visit(procediment.instructions)
        # Ja no necessitem les variables del scope
        self.var_scope_stack.pop()

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx):
        # Visita i defineix els procediments del fitxer .jsb
        self.visitChildren(ctx)
        # Executa el fitxer des de la funció d'entrada
        self.executeProc(self.entry, self.params)

    # Visit a parse tree produced by jsbachParser#defProc.
    def visitDefProc(self, ctx):
        name = ctx.PROCNAME().getText()

        # PROCNAME(0) PARAMS(1...)
        params_index = 1
        params = []
        # Iterem sobre els parametres fins que trobem el bracket que inicia el bloc
        while ctx.getChild(params_index).getText() != "|:":
            tmp = ctx.getChild(params_index).getText()
            if tmp not in params:
                params.append(tmp)
            else:
                raise JSBachError(
                    f"Procediment \"{name}\" té el paràmetre {tmp} duplicat en la seva definició.")
            params_index += 1

        self.procediments[name] = Procediment(name, params, ctx.cjtInstr())

    # Visit a parse tree produced by jsbachParser#invProc.
    def visitInvProc(self, ctx):
        name = ctx.PROCNAME().getText()

        if name not in self.procediments.keys():
            raise JSBachError(f"El procediment \"{name}\" no està definit.")
        else:
            # PROCNAME(0) PARAMS(1...)
            params_index = 1
            inv_params = []

            # Iterem sobre tots els paràmetres del procediment
            # menys 1 que es el nom del propi procediment
            while params_index < ctx.getChildCount():
                value = self.visit(ctx.getChild(params_index))
                inv_params.append(value)
                params_index += 1

            self.executeProc(name, inv_params)

    # Visit a parse tree produced by jsbachParser#cjtInstr.
    def visitCjtInstr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#instr.
    def visitInstr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.var_scope_stack[-1][var_name] = value

    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx):
        var_name = ctx.VAR().getText()
        value = input(">>> ")
        if (value.strip("-")).isnumeric():
            self.var_scope_stack[-1][var_name] = int(value)
        else:
            raise JSBachError(f"L'entrada només pot ser un enter")

    # Visit a parse tree produced by jsbachParser#write.
    def visitWrite(self, ctx):
        results = []
        for expr in ctx.expr():
            tmp = self.visit(expr)
            # Comprovem si l'expressió és una llista, per mostrar els elements separats per espais.
            if isinstance(tmp, list):
                # if len(tmp) == 0:
                #     raise JSBachError(f"La llista és buida.")
                results.append(" ".join(tmp))
            elif isinstance(tmp, dict):
                results.append(str(list(tmp.keys()))[2:-2])
            else:
                results.append(str(tmp))
        print(" ".join(results))

    # Visit a parse tree produced by jsbachParser#play.
    # TODO play instruction
    def visitPlay(self, ctx):
        # return self.visitChildren(ctx)
        for expr in ctx.expr():
            print(expr)

    # Visit a parse tree produced by jsbachParser#conditional.
    def visitConditional(self, ctx):
        if self.visit(ctx.exprCond()):
            self.visit(ctx.cjtInstr(0))
        elif ctx.getChildCount() > 5 and ctx.getChild(5).getText() == 'else':
            self.visit(ctx.cjtInstr(1))

    # Visit a parse tree produced by jsbachParser#while_.
    def visitWhile_(self, ctx):
        while self.visit(ctx.exprCond()):
            self.visit(ctx.cjtInstr())

    # Visit a parse tree produced by jsbachParser#addList.
    # TODO addList instruction
    def visitAddList(self, ctx):
        list_name = ctx.VAR().getText()
        llista = []
        if list_name in self.var_scope_stack[0].keys():
            llista = self.var_scope_stack[0][list_name]
        llista.append(str(self.visit(ctx.expr())))
        return llista

    # Visit a parse tree produced by jsbachParser#cutList.
    # TODO cutList instruction
    def visitCutList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#Cond.
    def visitCond(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text

        operation = {
            '==': lambda: left == right,
            '/=': lambda: left != right,
            '<': lambda: left < right,
            '<=': lambda: left <= right,
            '>': lambda: left > right,
            '>=': lambda: left >= right
        }
        return operation.get(op, lambda: None)()

    # Visit a parse tree produced by jsbachParser#InfixOp.
    def visitInfixOp(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = ctx.op.text
        # Comprovem divisió entre 0
        if op == "/" and right == 0:
            raise JSBachError(f"Divisió entre 0.")

        operation = {
            '*': lambda: left * right,
            '/': lambda: left / right,
            '+': lambda: left + right,
            '-': lambda: left - right,
            '%': lambda: left % right
        }

        if isinstance(left, dict):
            key = str(list(left.keys()))[2:-2]
            left = self.notes[key]

        if isinstance(right, dict):
            key = str(list(right.keys()))[2:-2]
            right = self.notes[key]

        result = operation.get(op, lambda: None)()
        return result

    # Visit a parse tree produced by jsbachParser#Paren.
    def visitParen(self, ctx):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by jsbachParser#List.
    # TODO visitList instruction
    def visitList(self, ctx):
        llista = []
        # Iterem sobre els fills menys els '{' '}' del
        i = 1
        while i <= ctx.getChildCount()-2:
            llista.append(str(self.visit(ctx.getChild(i))))
            i += 1
        return llista

    # Visit a parse tree produced by jsbachParser#ListElement.
    # TODO visitListElement instruction
    def visitListElement(self, ctx):
        return self.visitChildren(ctx)
        # list_name = ctx.VAR(0).getText()
        # print(list_name)
        # i = self.visit(ctx.op)
        # print(i)
        # if list_name in self.var_scope_stack[-1].keys():
        #     llista = self.var_scope_stack[-1][list_name]
        # else:
        #     raise JSBachError(f"La llista")

    # Visit a parse tree produced by jsbachParser#Note.
    # TODO Note token
    def visitNote(self, ctx):
        # return self.visitChildren(ctx)
        nota = {ctx.getText(): self.notes[ctx.getText()]}
        return nota

    # Visit a parse tree produced by jsbachParser#Variables.
    def visitVariables(self, ctx):
        var_name = ctx.VAR().getText()
        if var_name in self.var_scope_stack[-1].keys():
            return self.var_scope_stack[-1][var_name]
        else:
            raise JSBachError(f"Variable \" {var_name}\" no està definida.")

    # Visit a parse tree produced by jsbachParser#Numbers.
    def visitNumbers(self, ctx):
        value = ctx.getText()
        return int(value)

    # Visit a parse tree produced by jsbachParser#Strings.
    def visitStrings(self, ctx):
        # Només agafem el text entre les " "
        value = ctx.getText()[1:-1]
        return value
