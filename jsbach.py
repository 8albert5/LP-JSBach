from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from jsbachVisitor import jsbachVisitor
import sys

programa = sys.argv[1]
input_stream = FileStream(programa, encoding = 'utf-8')
print(f"Executant programa \"{programa}\"\n")

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = jsbachParser(token_stream)
tree = parser.root()

print(tree.toStringTree(recog=parser))