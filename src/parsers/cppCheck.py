"""A implementation of a parser for the cppcheck utility"""

from parsers.aParser import Parser


class CppCheckParser(Parser):

    def __init__(self, targetDir):
        super().__init__(targetDir)
