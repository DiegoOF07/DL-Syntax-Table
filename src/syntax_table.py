from first_follow import get_first_of_secuence
from grammar import Grammar


def build_table(grammar: Grammar, FIRST, FOLLOW):

    table = {
        A: {t: None for t in grammar.terminals.union({"$"})}
        for A in grammar.non_terminals
    }

    conflicts = []

    for A in grammar.non_terminals:
        for production in grammar.get_productions(A):

            first_alpha = get_first_of_secuence(production, grammar, FIRST)

            for terminal in first_alpha - {"ε"}:
                if table[A][terminal] is not None:
                    conflicts.append((A, terminal, table[A][terminal], production))
                table[A][terminal] = production

            if "ε" in first_alpha:
                for terminal in FOLLOW[A]:
                    if table[A][terminal] is not None:
                        conflicts.append((A, terminal, table[A][terminal], production))
                    table[A][terminal] = production

    return table, conflicts

def print_table(table, grammar):
    terminals = sorted(list(grammar.terminals)) + ["$"]

    col_width = 12

    # Header
    header = ["NT / T"] + terminals
    print("".join(col.ljust(col_width) for col in header))

    for A in sorted(grammar.non_terminals):
        row = [A]

        for t in terminals:
            production = table[A].get(t)

            if production:
                prod_str = f"{A}→{' '.join(production)}"
                row.append(prod_str)
            else:
                row.append("")

        print("".join(col.ljust(col_width) for col in row))

def is_ll1(conflicts):
    return len(conflicts) == 0