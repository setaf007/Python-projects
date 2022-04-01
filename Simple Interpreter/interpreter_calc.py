#Token types
INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'
)

class Token(object):
    def __init__(self, type, value):
        #token type: INTEGER, PLUS, MINUS, MUL, DIV OR EOF
        self.type = type
        #token value: non negative integer, +, -, *, / or None
        self.value = value

    #method called when print() or str() function invoked
    def __str__(self):
        """
        String representation of class instance
        e.g. Token(INTEGER, 3) OR Token(PLUS, '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    #repr returns object representation in string format
    def __repr__(self):
        return self.__str__()

class Lexer(object):
    def __init__(self, text):
        #user input text
        self.text = text
        #self.pos is index into self.text
        self.pos = 0
        #current token instance
        self.current_char = self.text[self.pos]
    
    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        #Advance pos pointer and set the current_char variable
        self.pos+=1
        if self.pos > len(self.text) - 1:
            self.current_char = None #indicater of eof
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        #Return a multidigit integer consumed from the input
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self):
        """
        Lexical analyzer (also know as scanner or tokenizer)
        Method responsible for breaking a sentence apart into tokens one at a time
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()
        
        return Token(EOF, None)

class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        #set current token to 1st token from input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        """
        compare current token type with passed token type, and if match, 'eat' the current token
        and assign the next token to the self.current_token, otherwise, raise exception
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        #factor : INTEGER
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result
    
    def term(self):
        #term : factor((MUL | DIV) factor)*
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()
        return result

    def expr(self):
        """
        Arithmetic expression parser/ interpreter
        expr : term ((PLUS | MINUS) term)*
        term : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print (result)

if __name__ == '__main__':
    main()
        
            
