class Token(object):
    def __repr__(self):
        value = getattr(self, "value", "")
        return f"{self.__class__.__name__}({value})"


class StreamStartToken(Token):
    id = "<stream start>"


class StreamEndToken(Token):
    id = "<stream end>"


class BlockStartToken(Token):
    id = "{"


class BlockEndToken(Token):
    id = "}"


class ValueToken(Token):
    id = ":"


class LiteralToken(Token):
    id = "<literal>"

    def __init__(self, value):
        self.value = value


class QuotedLiteralToken(Token):
    id = "<quoted literal>"

    def __init__(self, value):
        self.value = value
