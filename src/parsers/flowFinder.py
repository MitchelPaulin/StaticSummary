"""A implementation of a parser for the flowfinder utility"""

from parsers.aParser import Parser


class FlowFinderParser(Parser):

    def __init__(self, targetDir):
        super().__init__(targetDir)
