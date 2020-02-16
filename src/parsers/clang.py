"""A implementation of a parser for the clang utility"""

from parsers.aParser import Parser


class ClangParser(Parser):

    def __init__(self, targetDir: str):
        super().__init__(targetDir)
