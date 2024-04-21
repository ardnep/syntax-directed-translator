class Parser:
    def __init__(self):
        self.input = input("Enter an infix expression: ")
        self.idx = 0
        self.lookahead = self.input[0]

    def expr(self):
        self.term()
        while True:
            if self.lookahead == "+":
                self.match("+")
                self.term()
                print("+", end="")
            elif self.lookahead == "-":
                self.match("-")
                self.term()
                print("-", end="")
            else:
                return

    def term(self):
        if self.lookahead.isdigit():
            print(self.lookahead, end="")
            self.match(self.lookahead)
        else:
            raise SyntaxError("Syntax error")

    def match(self, t):
        if self.lookahead == t:
            self.idx += 1
            if self.idx < len(self.input):
                self.lookahead = self.input[self.idx]
        else:
            raise SyntaxError("Syntax error")


def main():
    parser = Parser()
    parser.expr()
    print()


if __name__ == "__main__":
    main()
