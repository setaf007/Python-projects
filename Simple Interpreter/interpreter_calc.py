#Token types
from multiprocessing.sharedctypes import Value


INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        #token type: INTEGER, PLUS, MINUS OR EOF
        self.type = type
        #token value: non negative integer, +, - or None
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

class Interpreter(object):
    def __init__(self, text):
        #user input text
        self.text = text
        #self.pos is index into self.text
        self.pos = 0
        #current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]
    
    def error(self):
        raise Exception('Error parsing input')

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

            self.error()
        
        return Token(EOF, None)

    def eat(self, token_type):
        """
        compare current token type with passed token type, and if match, 'eat' the current token
        and assign the next token to the self.current_token, otherwise, raise exception
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
        
    def expr(self):
        #expr -> INTEGER PLUS INTEGER
        #set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        #current token expected to be a single digit integer
        left = self.current_token
        self.eat(INTEGER)
        #current token expected to be a '+' or '-' token
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)
        #current token expected to be a single digit integer
        right = self.current_token
        self.eat(INTEGER)

        """
        after the above call, self.current_token is set to EOF token
        at this point, INTEGER PLUS/MINUS INTEGER sequence of tokens has been successfull found and the method
        can just return the result of adding two integers, successfully interpreting user input
        """
        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value

        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print (result)

if __name__ == '__main__':
    main()
        
            
