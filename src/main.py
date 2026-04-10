from parser import parse_grammar_from_file
from first_follow import get_first, get_follow

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