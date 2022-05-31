from antlr4 import *
from jsbachLexer import jsbachLexer
from jsbachParser import jsbachParser
from jsbachTreeVisitor import JSBachTreeVisitor
from jsbachTreeVisitor import JSBachError
from jsbachScript import runJSBachScript
import sys

programa = sys.argv[1]
input_stream = FileStream(programa, encoding='utf-8')
print(f"Executant programa \"{programa}\"\n")

lexer = jsbachLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = jsbachParser(token_stream)
tree = parser.root()

if len(sys.argv) == 3:
    visitor = JSBachTreeVisitor(sys.argv[2])
elif len(sys.argv) > 3:
    visitor = JSBachTreeVisitor(
        sys.argv[2], [int(param) for param in sys.argv[3:]])
else:
    visitor = JSBachTreeVisitor()

try:
    visitor.visit(tree)
    partitura = ' '.join(JSBachTreeVisitor.partitura)
    if len(partitura) == 0:
        print(f"El programa \"{programa}\" no ha generat una partitura vàlida (no buida).")
    else:
        runJSBachScript(programa[:-4], partitura)
except JSBachError as e:
    print(e.message)
