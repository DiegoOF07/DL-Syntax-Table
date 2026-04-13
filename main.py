import os
from src.parser import parse_grammar_from_file
from src.first_follow import get_first, get_follow
from src.syntax_table import build_table, print_table, is_ll1

def analyze_grammar(grammar, name=""):
    if name:
        print(f"\n{name}")
 
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
        print("\nTabla:")
        print_table(table, grammar)
    else:
        print("\nLa gramática NO es LL(1). Conflictos encontrados:")
        for A, terminal, prod1, prod2 in conflicts:
            print(f"  Conflicto en {A} con terminal '{terminal}':")
            print(f"    Producción 1: {A} -> {' '.join(prod1)}")
            print(f"    Producción 2: {A} -> {' '.join(prod2)}")

    

def load_and_analyze_file(filepath, name):
    try:
        grammar = parse_grammar_from_file(filepath)
        analyze_grammar(grammar, name)
    except Exception as e:
        print(f"\nError al procesar '{filepath}': {e}")
 
 
if __name__ == "__main__":
    grammars_dir = "./grammars"
 
    grammar_names = {
        "01_grammar.txt": "Gramática 1: Expresiones Aritméticas",
        "02_grammar.txt": "Gramática 2: Sentencias if-else (Dangling Else)",
        "03_grammar.txt": "Gramática 3: Expresiones Booleanas",
    }
 
    if not os.path.isdir(grammars_dir):
        print(f"Directorio '{grammars_dir}' no encontrado.")
    else:
        grammar_files = sorted([f for f in os.listdir(grammars_dir) if f.endswith(".txt")])
        if not grammar_files:
            print(f"No se encontraron archivos .txt en '{grammars_dir}'.")
        else:
            for filename in grammar_files:
                filepath = os.path.join(grammars_dir, filename)
                name = grammar_names.get(filename, filename)
                load_and_analyze_file(filepath, name)
 
    print("\nAnálisis completado.\n")

