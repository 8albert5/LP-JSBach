import imp


if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
    from .jsbachVisitor import jsbachVisitor
else:
    from jsbachParser import jsbachParser
    from jsbachVisitor import jsbachVisitor
    
# Aquesta classe defineix els errors més comuns de JSBach
class jsbachError(Exception):
    def __init__(self, msg):
        self.message = f"JSBachError: {msg}"
        
class jsbachTreeVisitor(jsbachVisitor):
    
    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#defProc.
    def visitDefProc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#cjtInstr.
    def visitCjtInstr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#instr.
    def visitInstr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#write.
    def visitWrite(self, ctx):
        results = []
        for expr in ctx.expr():
            results.append(str(self.visit(expr)))
        print(" ".join(results))


    # Visit a parse tree produced by jsbachParser#play.
    def visitPlay(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#invProc.
    def visitInvProc(self, ctx):
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
    def visitAddList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#cutList.
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
        return operation.get(op, lambda: None)()
        

    # Visit a parse tree produced by jsbachParser#Paren.
    def visitParen(self, ctx):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by jsbachParser#List.
    def visitList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ListElement.
    def visitListElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Note.
    def visitNote(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Variables.
    def visitVariables(self, ctx):
        var_name = ctx.VAR.getText()
        if var_name in self.var_scope_stack[-1].keys():
            return self.var_scope_stack[-1].var_name
        else:
            raise jsbachError(f"Variable \" {var_name}\" no està definida.")


    # Visit a parse tree produced by jsbachParser#Numbers.
    def visitNumbers(self, ctx):
        value = ctx.getText()
        return int(value)


    # Visit a parse tree produced by jsbachParser#Strings.
    def visitStrings(self, ctx):
        # Només agafem el text entre les " "
        value = ctx.getText()[1:-1]
        return value
