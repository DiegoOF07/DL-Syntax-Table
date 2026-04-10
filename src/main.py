from parser import parse_grammar_from_file
from first_follow import get_first, get_follow
from syntax_table import build_table, print_table, is_ll1

grammar = parse_grammar_from_file("./grammars/01_grammar.txt")

FIRST = get_first(grammar)
FOLLOW = get_follow(grammar, FIRST)

print(grammar.__str__())
print("\nFIRST:")
for k, v in FIRST.items():
    print(k, v)

print("\nFOLLOW:")
for k, v in FOLLOW.items():
    print(k, v)

table, conflicts = build_table(grammar, FIRST, FOLLOW)
if is_ll1(conflicts):
    print("\nLa gramática es LL(1)")
else:
    print("\nLa gramática NO es LL(1). Conflictos encontrados:")
    for A, terminal, prod1, prod2 in conflicts:
        print(f"  Conflicto en {A} con terminal '{terminal}':")
        print(f"    Producción 1: {A} -> {' '.join(prod1)}")
        print(f"    Producción 2: {A} -> {' '.join(prod2)}")

print("\nTabla:")
print_table(table, grammar)

