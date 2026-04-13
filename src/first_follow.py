from src.grammar import Grammar

def get_first(grammar: Grammar):
    FIRST = { A: set() for A in grammar.non_terminals }

    changed = True
    while changed:
        changed = False

        for A in grammar.non_terminals:
            for production in grammar.get_productions(A):

                # Caso ε
                if production == ["ε"]:
                    if "ε" not in FIRST[A]:
                        FIRST[A].add("ε")
                        changed = True
                    continue

                for symbol in production:

                    # Terminal
                    if grammar.is_terminal(symbol):
                        if symbol not in FIRST[A]:
                            FIRST[A].add(symbol)
                            changed = True
                        break

                    # No terminal
                    before = len(FIRST[A])
                    FIRST[A] |= (FIRST[symbol] - {"ε"})

                    if "ε" not in FIRST[symbol]:
                        break
                    else:
                        # Si es el último y todos derivan
                        if symbol == production[-1]:
                            FIRST[A].add("ε")

                    if len(FIRST[A]) > before:
                        changed = True

    return FIRST

def get_first_of_secuence(symbols, grammar: Grammar, FIRST):
    result = set()

    for symbol in symbols:

        if symbol == "ε":
            result.add("ε")
            return result

        if grammar.is_terminal(symbol):
            result.add(symbol)
            return result

        result |= (FIRST[symbol] - {"ε"})

        if "ε" not in FIRST[symbol]:
            return result

    result.add("ε")
    return result

def get_follow(grammar: Grammar, FIRST):
    FOLLOW = { A: set() for A in grammar.non_terminals }

    # Simbolo inicial
    FOLLOW[grammar.start_symbol].add("$")

    changed = True
    while changed:
        changed = False

        for A in grammar.non_terminals:
            for production in grammar.get_productions(A):

                for i in range(len(production)):
                    B = production[i]

                    if not grammar.is_non_terminal(B):
                        continue

                    beta = production[i+1:]

                    if beta:
                        first_beta = get_first_of_secuence(beta, grammar, FIRST)

                        before = len(FOLLOW[B])
                        FOLLOW[B] |= (first_beta - {"ε"})

                        if "ε" in first_beta:
                            FOLLOW[B] |= FOLLOW[A]

                        if len(FOLLOW[B]) > before:
                            changed = True

                    else:
                        before = len(FOLLOW[B])
                        FOLLOW[B] |= FOLLOW[A]

                        if len(FOLLOW[B]) > before:
                            changed = True

    return FOLLOW