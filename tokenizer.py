import re

class Tokenizer:
    def __init__(self, input):
        self.start = 0
        self.current = 0
        self.input = input
        self.tokens = []

    def consume(self):
        self.current += 1
        return self.cur_char()

    def get(self, idx):
        if idx >= len(self.input):
            return None
        return self.input[idx]

    # note: can return None
    def peek(self, amount):
        return self.get(self.current + amount)

    def pop(self):
        self.tokens.append(self.input[self.start:self.current])
        self.start = self.current

    def skip(self):
        self.consume()
        self.start = self.current

    def cur_char(self):
        return self.get(self.current)

    def at_end(self):
        return self.current >= len(self.input)

    def tokenize(self):
        while True:
            # whitespaces and newlines
            cur = self.cur_char()
            if cur is None:
                break
            if re.match('\s', cur) is not None:
                self.skip()
            # words
            elif cur.isalpha():
                self.consume()
                while True:
                    cur = self.cur_char()
                    if cur is None:
                        break
                    if not cur.isalpha():
                        break
                    self.consume()
                self.pop()
            # numbers and floats
            elif cur.isdigit():
                self.consume()
                while True:
                    cur = self.cur_char()
                    if cur is None:
                        break
                    if not cur.isdigit():
                        break
                    self.consume()
                if cur == '.':
                    next = self.peek(1)
                    if next is not None and next.isdigit():
                        cur = self.consume()  # '.'
                        self.consume()  # consider omitting it
                        while True:
                            cur = self.cur_char()
                            if cur is None:
                                break
                            if not cur.isdigit():
                                break
                            self.consume()
                self.pop()
            # floats starting with '.'
            elif cur == '.':
                cur = self.consume()
                if cur is None:
                    pass
                elif cur.isdigit():
                    while True:
                        cur = self.cur_char()
                        if cur is None:
                            break
                        if not cur.isdigit():
                            break
                        self.consume()
                self.pop()
                # punctuation marks
            else:
                self.consume()
                self.pop()
        return self.tokens

def tokenize(input):
    return Tokenizer(input).tokenize()
