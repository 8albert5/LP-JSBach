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


    # Visit a parse tree produced by jsbachParser#play.
    def visitPlay(self, ctx:jsbachParser.PlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#invProc.
    def visitInvProc(self, ctx:jsbachParser.InvProcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#conditional.
    def visitConditional(self, ctx:jsbachParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#while_.
    def visitWhile_(self, ctx:jsbachParser.While_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#addList.
    def visitAddList(self, ctx:jsbachParser.AddListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#cutList.
    def visitCutList(self, ctx:jsbachParser.CutListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Cond.
    def visitCond(self, ctx:jsbachParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Variables.
    def visitVariables(self, ctx:jsbachParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Numbers.
    def visitNumbers(self, ctx:jsbachParser.NumbersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Note.
    def visitNote(self, ctx:jsbachParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#ListElement.
    def visitListElement(self, ctx:jsbachParser.ListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Modul.
    def visitModul(self, ctx:jsbachParser.ModulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#List.
    def visitList(self, ctx:jsbachParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#InfixOp.
    def visitInfixOp(self, ctx:jsbachParser.InfixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Strings.
    def visitStrings(self, ctx:jsbachParser.StringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsbachParser#Paren.
    def visitParen(self, ctx:jsbachParser.ParenContext):
        return self.visitChildren(ctx)



del jsbachParser