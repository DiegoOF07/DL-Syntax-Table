from src.grammar import Grammar


def parse_grammar_lines(lines):
    grammar = None

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if "->" not in line:
            raise ValueError(f"Línea inválida: {line}")

        lhs, rhs = line.split("->")
        lhs = lhs.strip()

        if grammar is None:
            grammar = Grammar(start_symbol=lhs)

        productions = rhs.split("|")

        for prod in productions:
            symbols = prod.strip().split()
            grammar.add_production(lhs, symbols)

    if grammar is None:
        raise ValueError("No se pudo parsear la gramática")

    grammar.compute_terminals()

    return grammar


def parse_grammar_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return parse_grammar_lines(lines)