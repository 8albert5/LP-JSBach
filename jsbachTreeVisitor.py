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


class jsbachTreeVisitor(jsbachVisitor):
    def __init__(self, entry="Main", params=[]):
        self.entry = entry
        self.params = params

        self.varScopeStack = []
        self.procediments = {}

    def executeProc(self, name, params):
        procediment = self.procediments[name]
        expectedParams = len(procediment.params)

        # Comprovem si el procediment té el número de paràmetres correcte.
        if expectedParams != len(params):
            raise JSBachError(
                f"Procediment \"{name}\" espera {expectedParams} paràmetres i n'ha rebut {len(params)}.")

        # Creem el diccionari de variable -> valor
        variables = {}
        for varName, value in zip(procediment.params, params):
            variables[varName] = value

        # Afegim nou scope de variables a la pila
        self.varScopeStack.append(variables)
        # L'execució fa servir l'element de la pila
        self.visit(procediment.instructions)
        # Ja no necessitem les variables del scope
        self.varScopeStack.pop()

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
        paramsIndex = 1
        params = []
        # Iterem sobre els parametres fins que trobem el bracket que inicia el bloc
        while ctx.getChild(paramsIndex).getText() != "|:":
            tmp = ctx.getChild(paramsIndex).getText()
            if not tmp in params:
                params.append(tmp)
            else:
                raise JSBachError(
                    f"Procediment \"{name}\" té el paràmetre {tmp} duplicat en la seva definició.")
            paramsIndex += 1

        self.procediments[name] = Procediment(name, params, ctx.cjtInstr())

    # Visit a parse tree produced by jsbachParser#invProc.
    def visitInvProc(self, ctx):
        name = ctx.PROCNAME().getText()

        if not name in self.procediments.keys():
            raise JSBachError(f"El procediment \"{name}\" no està definit.")
        else:
            # PROCNAME(0) PARAMS(1...)
            paramsIndex = 1
            invParams = []

            # Iterem sobre tots els paràmetres del procediment
            # menys 1 que es el nom del propi procediment
            while paramsIndex < ctx.getChildCount():
                value = self.visit(ctx.getChild(paramsIndex))
                invParams.append(value)
                paramsIndex += 1

            self.executeProc(name, invParams)

    # Visit a parse tree produced by jsbachParser#cjtInstr.
    def visitCjtInstr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#instr.
    def visitInstr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx):
        varName = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.varScopeStack[-1][varName] = value

    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx):
        varName = ctx.VAR().getText()
        value = input(">>> ")
        if (value.strip("-")).isnumeric():
            self.varScopeStack[-1][varName] = int(value)
        else:
            raise JSBachError(f"L'entrada només pot ser un enter")

    # Visit a parse tree produced by jsbachParser#write.
    def visitWrite(self, ctx):
        results = []
        for expr in ctx.expr():
            results.append(str(self.visit(expr)))
        print(" ".join(results))

    # Visit a parse tree produced by jsbachParser#play.
    # TODO play instruction
    def visitPlay(self, ctx):
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

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

        operation = {
            '*': lambda: left * right,
            '/': lambda: left / right,
            '+': lambda: left + right,
            '-': lambda: left - right,
            '%': lambda: left % right
        }
        # Comprovem divisió entre 0
        if op == "/" and right == 0:
            raise JSBachError(f"Divisió entre 0.")

        return operation.get(op, lambda: None)()

    # Visit a parse tree produced by jsbachParser#Paren.
    def visitParen(self, ctx):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by jsbachParser#List.
    # TODO visitList instruction
    def visitList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#ListElement.
    # TODO visitListElement instruction
    def visitListElement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#Note.
    # TODO Note token
    def visitNote(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by jsbachParser#Variables.
    def visitVariables(self, ctx):
        varName = ctx.VAR().getText()
        if varName in self.varScopeStack[-1].keys():
            return self.varScopeStack[-1][varName]
        else:
            raise JSBachError(f"Variable \" {varName}\" no està definida.")

    # Visit a parse tree produced by jsbachParser#Numbers.
    def visitNumbers(self, ctx):
        value = ctx.getText()
        return int(value)

    # Visit a parse tree produced by jsbachParser#Strings.
    def visitStrings(self, ctx):
        # Només agafem el text entre les " "
        value = ctx.getText()[1:-1]
        return value
