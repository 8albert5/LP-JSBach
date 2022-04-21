# Generated from jsbach.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3#")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\5\3#\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\3\5\5\5\62")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b>\n\b")
        buf.write("\f\b\16\bA\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\tO\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t`\n\t\f\t\16\tc\13\t\3\t")
        buf.write("\2\3\20\n\2\4\6\b\n\f\16\20\2\2\2l\2\25\3\2\2\2\4\32\3")
        buf.write("\2\2\2\6+\3\2\2\2\b\61\3\2\2\2\n\63\3\2\2\2\f\67\3\2\2")
        buf.write("\2\16:\3\2\2\2\20N\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2")
        buf.write("\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2")
        buf.write("\2\27\25\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2\2\32\"\7\35")
        buf.write("\2\2\33\37\7\36\2\2\34\36\7\36\2\2\35\34\3\2\2\2\36!\3")
        buf.write("\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 #\3\2\2\2!\37\3\2\2\2")
        buf.write("\"\33\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7\33\2\2%&\5\6\4")
        buf.write("\2&\'\7\34\2\2\'\5\3\2\2\2(*\5\b\5\2)(\3\2\2\2*-\3\2\2")
        buf.write("\2+)\3\2\2\2+,\3\2\2\2,\7\3\2\2\2-+\3\2\2\2.\62\5\n\6")
        buf.write("\2/\62\5\f\7\2\60\62\5\16\b\2\61.\3\2\2\2\61/\3\2\2\2")
        buf.write("\61\60\3\2\2\2\62\t\3\2\2\2\63\64\7\36\2\2\64\65\7\3\2")
        buf.write("\2\65\66\5\20\t\2\66\13\3\2\2\2\678\7\4\2\289\7\36\2\2")
        buf.write("9\r\3\2\2\2:;\7\5\2\2;?\5\20\t\2<>\5\20\t\2=<\3\2\2\2")
        buf.write(">A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\17\3\2\2\2A?\3\2\2\2B")
        buf.write("C\b\t\1\2CD\7\27\2\2DE\5\20\t\2EF\7\30\2\2FO\3\2\2\2G")
        buf.write("H\7\31\2\2HI\5\20\t\2IJ\7\32\2\2JO\3\2\2\2KO\7\36\2\2")
        buf.write("LO\7\37\2\2MO\7 \2\2NB\3\2\2\2NG\3\2\2\2NK\3\2\2\2NL\3")
        buf.write("\2\2\2NM\3\2\2\2Oa\3\2\2\2PQ\f\f\2\2QR\7\16\2\2R`\5\20")
        buf.write("\t\rST\f\13\2\2TU\7\17\2\2U`\5\20\t\fVW\f\n\2\2WX\7\20")
        buf.write("\2\2X`\5\20\t\13YZ\f\t\2\2Z[\7\f\2\2[`\5\20\t\n\\]\f\b")
        buf.write("\2\2]^\7\r\2\2^`\5\20\t\t_P\3\2\2\2_S\3\2\2\2_V\3\2\2")
        buf.write("\2_Y\3\2\2\2_\\\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2")
        buf.write("b\21\3\2\2\2ca\3\2\2\2\13\25\37\"+\61?N_a")
        return buf.getvalue()


class jsbachParser ( Parser ):

    grammarFileName = "jsbach.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<-'", "'<?>'", "'<!>'", "'<:>'", "'if'", 
                     "'else'", "'while'", "'<<'", "'8<'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'='", "'/='", "'<'", "'<='", 
                     "'>'", "'>='", "'('", "')'", "'{'", "'}'", "'|:'", 
                     "':|'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "READ", "WRITE", "PLAY", "IF", 
                      "ELSE", "WHILE", "ADD", "CUT", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "EQ", "NEQ", "LT", "LET", "GT", "GET", 
                      "LP", "RP", "LB", "RB", "OB", "CB", "PROCNAME", "VAR", 
                      "NUM", "STRING", "IDENTIFIER", "COMMENT", "WS" ]

    RULE_root = 0
    RULE_defProc = 1
    RULE_cjtInstr = 2
    RULE_instr = 3
    RULE_assign = 4
    RULE_read = 5
    RULE_write = 6
    RULE_expr = 7

    ruleNames =  [ "root", "defProc", "cjtInstr", "instr", "assign", "read", 
                   "write", "expr" ]

    EOF = Token.EOF
    ASSIGN=1
    READ=2
    WRITE=3
    PLAY=4
    IF=5
    ELSE=6
    WHILE=7
    ADD=8
    CUT=9
    PLUS=10
    MINUS=11
    MULT=12
    DIV=13
    MOD=14
    EQ=15
    NEQ=16
    LT=17
    LET=18
    GT=19
    GET=20
    LP=21
    RP=22
    LB=23
    RB=24
    OB=25
    CB=26
    PROCNAME=27
    VAR=28
    NUM=29
    STRING=30
    IDENTIFIER=31
    COMMENT=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(jsbachParser.EOF, 0)

        def defProc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.DefProcContext)
            else:
                return self.getTypedRuleContext(jsbachParser.DefProcContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = jsbachParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==jsbachParser.PROCNAME:
                self.state = 16
                self.defProc()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(jsbachParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefProcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCNAME(self):
            return self.getToken(jsbachParser.PROCNAME, 0)

        def OB(self):
            return self.getToken(jsbachParser.OB, 0)

        def cjtInstr(self):
            return self.getTypedRuleContext(jsbachParser.CjtInstrContext,0)


        def CB(self):
            return self.getToken(jsbachParser.CB, 0)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(jsbachParser.VAR)
            else:
                return self.getToken(jsbachParser.VAR, i)

        def getRuleIndex(self):
            return jsbachParser.RULE_defProc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefProc" ):
                return visitor.visitDefProc(self)
            else:
                return visitor.visitChildren(self)




    def defProc(self):

        localctx = jsbachParser.DefProcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_defProc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(jsbachParser.PROCNAME)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==jsbachParser.VAR:
                self.state = 25
                self.match(jsbachParser.VAR)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==jsbachParser.VAR:
                    self.state = 26
                    self.match(jsbachParser.VAR)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 34
            self.match(jsbachParser.OB)
            self.state = 35
            self.cjtInstr()
            self.state = 36
            self.match(jsbachParser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CjtInstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.InstrContext)
            else:
                return self.getTypedRuleContext(jsbachParser.InstrContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_cjtInstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCjtInstr" ):
                return visitor.visitCjtInstr(self)
            else:
                return visitor.visitChildren(self)




    def cjtInstr(self):

        localctx = jsbachParser.CjtInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cjtInstr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << jsbachParser.READ) | (1 << jsbachParser.WRITE) | (1 << jsbachParser.VAR))) != 0):
                self.state = 38
                self.instr()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(jsbachParser.AssignContext,0)


        def read(self):
            return self.getTypedRuleContext(jsbachParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(jsbachParser.WriteContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_instr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = jsbachParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.VAR]:
                self.state = 44
                self.assign()
                pass
            elif token in [jsbachParser.READ]:
                self.state = 45
                self.read()
                pass
            elif token in [jsbachParser.WRITE]:
                self.state = 46
                self.write()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(jsbachParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)


        def getRuleIndex(self):
            return jsbachParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = jsbachParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(jsbachParser.VAR)
            self.state = 50
            self.match(jsbachParser.ASSIGN)
            self.state = 51
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(jsbachParser.READ, 0)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def getRuleIndex(self):
            return jsbachParser.RULE_read

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = jsbachParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(jsbachParser.READ)
            self.state = 54
            self.match(jsbachParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(jsbachParser.WRITE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)


        def getRuleIndex(self):
            return jsbachParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = jsbachParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(jsbachParser.WRITE)
            self.state = 57
            self.expr(0)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.expr(0) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return jsbachParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariablesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(jsbachParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)


    class SumaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(jsbachParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class DivisioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def DIV(self):
            return self.getToken(jsbachParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivisio" ):
                return visitor.visitDivisio(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(jsbachParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def RP(self):
            return self.getToken(jsbachParser.RP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicacioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def MULT(self):
            return self.getToken(jsbachParser.MULT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacio" ):
                return visitor.visitMultiplicacio(self)
            else:
                return visitor.visitChildren(self)


    class ModulContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def MOD(self):
            return self.getToken(jsbachParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModul" ):
                return visitor.visitModul(self)
            else:
                return visitor.visitChildren(self)


    class LlistesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(jsbachParser.LB, 0)
        def expr(self):
            return self.getTypedRuleContext(jsbachParser.ExprContext,0)

        def RB(self):
            return self.getToken(jsbachParser.RB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlistes" ):
                return visitor.visitLlistes(self)
            else:
                return visitor.visitChildren(self)


    class NumerosContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(jsbachParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeros" ):
                return visitor.visitNumeros(self)
            else:
                return visitor.visitChildren(self)


    class StringsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(jsbachParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrings" ):
                return visitor.visitStrings(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a jsbachParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsbachParser.ExprContext)
            else:
                return self.getTypedRuleContext(jsbachParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(jsbachParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = jsbachParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [jsbachParser.LP]:
                localctx = jsbachParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 65
                self.match(jsbachParser.LP)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(jsbachParser.RP)
                pass
            elif token in [jsbachParser.LB]:
                localctx = jsbachParser.LlistesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(jsbachParser.LB)
                self.state = 70
                self.expr(0)
                self.state = 71
                self.match(jsbachParser.RB)
                pass
            elif token in [jsbachParser.VAR]:
                localctx = jsbachParser.VariablesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(jsbachParser.VAR)
                pass
            elif token in [jsbachParser.NUM]:
                localctx = jsbachParser.NumerosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                self.match(jsbachParser.NUM)
                pass
            elif token in [jsbachParser.STRING]:
                localctx = jsbachParser.StringsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(jsbachParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = jsbachParser.MultiplicacioContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 79
                        self.match(jsbachParser.MULT)
                        self.state = 80
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = jsbachParser.DivisioContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 82
                        self.match(jsbachParser.DIV)
                        self.state = 83
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = jsbachParser.ModulContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 85
                        self.match(jsbachParser.MOD)
                        self.state = 86
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = jsbachParser.SumaContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 88
                        self.match(jsbachParser.PLUS)
                        self.state = 89
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = jsbachParser.RestaContext(self, jsbachParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 91
                        self.match(jsbachParser.MINUS)
                        self.state = 92
                        self.expr(7)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




