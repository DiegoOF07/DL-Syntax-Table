class Grammar:
    def __init__(self, start_symbol):
        self.start_symbol = start_symbol
        self.productions: dict[str, list[str]] = {}
        self.non_terminals = set()
        self.terminals = set()

    def add_production(self, head, body):
        if head not in self.productions:
            self.productions[head] = []

        self.productions[head].append(body)
        self.non_terminals.add(head)

    def compute_terminals(self):
        symbols = set()

        for head in self.productions:
            for production in self.productions[head]:
                for symbol in production:
                    symbols.add(symbol)

        self.terminals = {
            s for s in symbols
            if s not in self.non_terminals and s != "ε"
        }

    def is_terminal(self, symbol):
        return symbol in self.terminals

    def is_non_terminal(self, symbol):
        return symbol in self.non_terminals

    def get_productions(self, non_terminal):
        return self.productions.get(non_terminal, [])

    def all_symbols(self):
        return self.non_terminals.union(self.terminals)
    
    def __str__(self):
        lines = []
        lines.append(f"Simbolo inicial: {self.start_symbol}\n")

        lines.append("Producciones:")
        for head in self.productions:
            bodies = [" ".join(prod) for prod in self.productions[head]]
            lines.append(f"  {head} -> {' | '.join(bodies)}")

        lines.append("\nNo terminales: " + ", ".join(sorted(self.non_terminals)))
        lines.append("Terminales: " + ", ".join(sorted(self.terminals)))

        return "\n".join(lines)