from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from jsbachTreeVisitor import jsbachTreeVisitor
from jsbachTreeVisitor import JSBachError
import sys

# programa = sys.argv[1]
# input_stream = FileStream(programa, encoding='utf-8')
# print(f"Executant programa \"{programa}\"\n")

# lexer = jsbachLexer(input_stream)
# token_stream = CommonTokenStream(lexer)

# parser = jsbachParser(token_stream)
# tree = parser.root()

# PER IMPRIMIR ELS PARSE TREES
# print(tree.toStringTree(recog=parser))

# PER PROVAR COSETES PER CONSOLA
data = InputStream(input(">>> "))
lexer = jsbachLexer(data)
stream = CommonTokenStream(lexer)

parser = jsbachParser(stream)
tree2 = parser.write()

visitor = jsbachTreeVisitor()
output = visitor.visit(tree2)
print(output)

# DEFINITIU (? -> S'HA DE PROVAR)
# if len(sys.argv) == 3:
#     visitor = jsbachTreeVisitor(sys.argv[2])
# elif len(sys.argv) > 3:
#     visitor = jsbachTreeVisitor(
#         sys.argv[2], [int(param) for param in sys.argv[3:]])
# else:
#     visitor = jsbachTreeVisitor()

# try:
#     visitor.visit(tree)
# except JSBachError as e:
#     print(e.message)
