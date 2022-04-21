# Generated from jsbach.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsbachParser import jsbachParser
else:
    from jsbachParser import jsbachParser

# This class defines a complete generic visitor for a parse tree produced by jsbachParser.

class jsbachVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsbachParser#root.
    def visitRoot(self, ctx:jsbachParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#defProc.
    def visitDefProc(self, ctx:jsbachParser.DefProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#cjtInstr.
    def visitCjtInstr(self, ctx:jsbachParser.CjtInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#instr.
    def visitInstr(self, ctx:jsbachParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#assign.
    def visitAssign(self, ctx:jsbachParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#read.
    def visitRead(self, ctx:jsbachParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#write.
    def visitWrite(self, ctx:jsbachParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Variables.
    def visitVariables(self, ctx:jsbachParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Suma.
    def visitSuma(self, ctx:jsbachParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Divisio.
    def visitDivisio(self, ctx:jsbachParser.DivisioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Parentesis.
    def visitParentesis(self, ctx:jsbachParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Multiplicacio.
    def visitMultiplicacio(self, ctx:jsbachParser.MultiplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Modul.
    def visitModul(self, ctx:jsbachParser.ModulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Llistes.
    def visitLlistes(self, ctx:jsbachParser.LlistesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Numeros.
    def visitNumeros(self, ctx:jsbachParser.NumerosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Strings.
    def visitStrings(self, ctx:jsbachParser.StringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Resta.
    def visitResta(self, ctx:jsbachParser.RestaContext):
        return self.visitChildren(ctx)



del jsbachParser