from markdownify import markdownify


class ParserBase:
    def __init__(self):
        pass

    def parse(self, content: str) -> bool:
        raise NotImplementedError

    def export(self) -> str:
        raise NotImplementedError


class HTMLParser(ParserBase):
    def __init__(self):
        super().__init__()

    def parse(self, content: str) -> bool:
        self.content = content
        return True

    def export(self) -> str:
        return markdownify(self.content)


def beautify(content: str) -> str:
    parsers = [
        HTMLParser(),
    ]

    for parser in parsers:
        if parser.parse(content):
            return parser.export()

    return content
